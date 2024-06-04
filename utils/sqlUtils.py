def groupTransaksi (transaksi) :
    groupedTransaksi = []
    for item in transaksi:
        found = False
        for group in groupedTransaksi:
            if group['idTransaksi'] == item['id_transaksi']:
                group['listBagianFurnitur'].append(item)
                found = True
                break

        if not found:
            new_group = {
                'idTransaksi': item['id_transaksi'],
                'listBagianFurnitur': [item]
            }
            groupedTransaksi.append(new_group)

    return groupedTransaksi