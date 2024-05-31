CREATE TABLE Furnitur (
	id_furnitur INT PRIMARY KEY IDENTITY,
	nama VARCHAR(100) UNIQUE NOT NULL,
	deskripsi VARCHAR(500) NOT NULL,
	url_foto_display VARCHAR(255) NOT NULL
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
);

CREATE TABLE Pengguna (
	id_pengguna INT PRIMARY KEY IDENTITY,
	username VARCHAR(50) NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(50) NOT NULL,
	nomor_telepon CHAR(14) NOT NULL UNIQUE,
	role VARCHAR(20) CHECK (role IN ('pemilik', 'pengguna')) NOT NULL,
	tanggal_daftar DATETIME DEFAULT GETDATE(),
	alamat VARCHAR(100) NOT NULL,
	id_kelurahan INT NOT NULL FOREIGN KEY REFERENCES Kelurahan(id_kelurahan)
);


CREATE TABLE Kecamatan (
	id_kecamatan INT NOT NULL IDENTITY PRIMARY KEY,
	nama VARCHAR(100)
);

CREATE TABLE Kelurahan (
	id_kelurahan INT NOT NULL IDENTITY PRIMARY KEY,
	nama VARCHAR(100),
	id_kecamatan INT FOREIGN KEY REFERENCES Kecamatan(id_kecamatan) NOT NULL,
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
	tanggal_transaksi DATETIME DEFAULT GETDATE(),
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


