from utils import get_data, get_filtered_data, get_last_values, get_data_output


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data)
    assert [x['date'] for x in data] == ['2019-08-26T10:50:58.294041',
                                         '2019-07-03T18:35:29.512364',
                                         '2019-04-04T23:20:05.206878',
                                         '2018-06-30T02:08:58.425572',
                                         '2018-06-30T02:08:58.425572']


def test_get_data_output(test_data):
    data = get_data_output(test_data[:1])
    assert data[0] == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 - > Счет **9589\n31957.58 руб.'
