CREATE TABLE Furnitur (
	id_furnitur INT PRIMARY KEY IDENTITY,
	nama VARCHAR(100) UNIQUE NOT NULL,
	deskripsi VARCHAR(500) NOT NULL,
	is_active BIT NOT NULL DEFAULT 1
);

CREATE TABLE Warna (
	id_warna INT PRIMARY KEY IDENTITY,
	nama VARCHAR(100) NOT NULL 
);

CREATE TABLE Material(
	id_material INT PRIMARY KEY IDENTITY,
	nama VARCHAR(100) NOT NULL
);

CREATE TABLE Bagian_Furnitur(
	id_bagian_furnitur INT PRIMARY KEY IDENTITY,
	nama VARCHAR(100) NOT NULL,
	panjang FLOAT NOT NULL,
	lebar FLOAT NOT NULL,
	tinggi FLOAT NOT NULL,
	id_furnitur INT NOT NULL FOREIGN KEY REFERENCES Furnitur(id_furnitur),
	is_active BIT NOT NULL DEFAULT 1
);

CREATE TABLE Kecamatan (
	id_kecamatan INT NOT NULL IDENTITY PRIMARY KEY,
	nama VARCHAR(100) NOT NULL
);

CREATE TABLE Kelurahan (
	id_kelurahan INT NOT NULL IDENTITY PRIMARY KEY,
	nama VARCHAR(100) NOT NULL,
	id_kecamatan INT NOT NULL FOREIGN KEY REFERENCES Kecamatan(id_kecamatan),
);

CREATE TABLE Pengguna (
	id_pengguna INT PRIMARY KEY IDENTITY,
	username VARCHAR(50) NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	nama VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	nomor_telepon CHAR(14) NOT NULL UNIQUE,
	role VARCHAR(20) CHECK (role IN ('pemilik', 'pelanggan')) NOT NULL DEFAULT 'pelanggan',
	tanggal_daftar DATETIME NOT NULL DEFAULT GETDATE(),
	alamat VARCHAR(100) NOT NULL,
	id_kelurahan INT NOT NULL FOREIGN KEY REFERENCES Kelurahan(id_kelurahan)
);


-- approach 1
-- composite primary key lalu direference ketiganya pada Transaksi_Bagian_Furnitur
CREATE TABLE Detail_Bagian_Furnitur(
	id_bagian_furnitur INT NOT NULL FOREIGN KEY REFERENCES Bagian_Furnitur(id_bagian_furnitur),
	id_warna INT NOT NULL FOREIGN KEY REFERENCES Warna(id_warna),
	id_material INT NOT NULL FOREIGN KEY REFERENCES Material(id_material),
	harga MONEY NOT NULL,
	stok INT NOT NULL,
	PRIMARY KEY (id_bagian_furnitur, id_warna, id_material)
);

CREATE TABLE Transaksi (
	id_transaksi INT NOT NULL IDENTITY PRIMARY KEY,
	id_pengguna INT NOT NULL FOREIGN KEY REFERENCES Pengguna(id_pengguna),
	id_furnitur INT NOT NULL FOREIGN KEY REFERENCES Furnitur(id_furnitur),
	tanggal_transaksi DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE Transaksi_Bagian_Furnitur (
	id_transaksi INT NOT NULL FOREIGN KEY REFERENCES Transaksi(id_transaksi),
	id_bagian_furnitur INT NOT NULL,
	id_warna INT NOT NULL,
	id_material INT NOT NULL,
	kuantitas INT NOT NULL,
	FOREIGN KEY (
		id_bagian_furnitur,
		id_warna,
		id_material
	)
	REFERENCES Detail_Bagian_Furnitur(
		id_bagian_furnitur,
		id_warna,
		id_material
	),
	PRIMARY KEY (id_transaksi, id_bagian_furnitur, id_warna, id_material)
);