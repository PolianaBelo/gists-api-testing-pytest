# SYSTEM DATA
in_home_api_url = 'wss://srbr30inhomeapi.ihtestsscesar.com/'

# LOGIN DATA
sc1_login = 'automation-sc'
sc1_password = 'Cesar@12'
sc_admin = 'automation-scadm1'
sc_admin_password = 'Cesar@12'
samsung_admin = 'automation-sam'
samsung_admin_password = 'Cesar@12'
samsung_admin_read_only = 'automation-samro'
samsung_admin_read_only_password = 'Cesar@12'

samsung_admin_sc_name = 'J.M.V. MANUTENCAO EM INFORMATICA LTDA'
sc_admin_sc_name = 'J.M.V. MANUTENCAO EM INFORMATICA LTDA'

# POST GIST PARAMETERS

valid_description_1 = "test_data"
valid_description_2 = "test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_" \
                      "test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_" \
                      "test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_" \
                      "test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_" \
                      "test_data"
valid_description_3 = "t"
valid_description_4 = "123456"
valid_description_5 = "!@#$%ˆˆ*()-_+=?><,./\\|ç"
valid_description_6 = ""

valid_file_1 = {"test.txt": {"content": "contents"}}
valid_file_2 = {"test.pdf": {"content": "contents_contents_contents_contents_contents_contents_contents_contents"}}
valid_file_3 = {"_1234abc": {"content": "123456789123456789123456789123456789123456789123456789123456789123456789"
                                        "123456789123456789123456789123456789123456789123456789123456789123456789"
                                        "123456789123456789123456789123456789123456789123456789123456789"}}
valid_file_4 = {"name_1.xls": {"content": "*************************************************************"}}
valid_file_5 = {"0name": {"content": "contents"}}
valid_file_6 = {"test.txt": {"content": "123ABC"}}

updated_description_1 = "new_test_data"
updated_description_2 = "test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_test_data_"
updated_description_3 = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
updated_description_4 = "_abc_123_"
updated_description_5 = ""
updated_description_6 = "(abc name_456789)"

updated_file_1 = {"new.txt": {"content": "contents"}}
updated_file_2 = {"test.txt": {"content": "contents_contents_contents_contents_contents_contents_contents_contents"}}
updated_file_3 = {"_abc.pdf": {"content": "123456789123456789123456789123456789123456789123456789123456789123456789"
                                        "123456789123456789123456789123456789123456789123456789123456789123456789"
                                        "123456789123456789123456789123456789123456789123456789123456789"}}
updated_file_4 = {"test.xls": {"content": "*************************************************************"}}
updated_file_5 = {"0_name_": {"content": "contents"}}
updated_file_6 = {"TEST.pdf": {"content": "123ABC"}}

POST_GIST_VALID_PARAMETERS = [(valid_description_1, valid_file_1, True),
                              (valid_description_2, valid_file_2, False),
                              (valid_description_3, valid_file_3, True),
                              (valid_description_4, valid_file_4, True),
                              (valid_description_5, valid_file_5, False),
                              (valid_description_6, valid_file_6, True)]

PATCH_GIST_VALID_PARAMETERS = [(updated_description_1, updated_file_1, True),
                               (updated_description_2, updated_file_2, False),
                               (updated_description_3, updated_file_3, True),
                               (updated_description_4, updated_file_4, True),
                               (updated_description_5, updated_file_5, False),
                               (updated_description_6, updated_file_6, True)]
