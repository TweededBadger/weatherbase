def get_table_data(tree,row_name,col_index):
    try:
        data = tree.xpath('.//tr[td="{0}"]'.format(row_name))[0].findall('td')[col_index].findall('b')[0].text
    except:
        try:
            data = tree.xpath('.//tr[td="{0}"]'.format(row_name))[0].findall('td')[col_index].text
        except:
            data = None

    return data