
#: DICT REFERENCE TO KNOW ALL WIDGET IN GLOVAL VAR
DATA_GLOBAL: dict = {
    'main_page': str(),

    'secundary_menu_show': False,
    'show_off': True,
    'text_size': 14,
}


def GLOBAL_VAR(
    set_global_var:        dict = {'var_name': 'value_in'},
    get_global_var:        str = 'var_name',
    remove_global_var:     str = 'var_remove',
    remove_screen_var:     str = 'var_screen_remove',
    remove_all_screen_var: bool = True,
    exist_key_in_dict:     str = "key_name",
    ):
    """
    #### GLOBAL_VAR IS A DICT THAT COINTEN ALL DATA THAT WE WANT CALL IN ALL FLET-BOX
    #### WE MAY CALL IN ALL MOMENT IMPORTING LITE CONFIG

    ### EXEMPLE:

    >>> from ..app_screen_db import GLOBAL_VAR

    ### Set the global var by Name and Value:

    >>> GLOBAL_VAR(set_global_var={'var_name':'value_in'})

    ### Get the gloval bar by name:

    >>> GLOBAL_VAR(get_global_var='var_name'})

    ### Remove the gloval bar by name:

    >>> GLOBAL_VAR(remove_global_var='var_remove'})
    """
    # global DATA_GLOBAL

    if not set_global_var == {'var_name': 'value_in'}:
        """ UPDATE DATABASE IF NO EXIST CREATE DATA IF EXIST OVERWRITE DATA"""
        DATA_GLOBAL.update(set_global_var)

    if not get_global_var == 'var_name':
        """ FIND SELECTED INPUT IN DATABASE IF NO EXIST RETURN THAT NO EXIST DATA"""
        TMP_DATA_GLOBAL = DATA_GLOBAL.get(
            get_global_var, "Please no exist input in database")
        return TMP_DATA_GLOBAL

    if not remove_global_var == 'var_remove':
        """ REMOVE SPECIFIC WIDGET FROM SELECTED WIDGET PHONE"""
        DATA_GLOBAL.get('EXPORT_DATA_PHONE').pop(remove_global_var)

    if remove_all_screen_var:
        """ REMOVE SPECIFIC WIDGET FROM SELECTED SCREEN PHONE"""
        DATA_GLOBAL['ALL_SCREEN_IN_DICT'] = dict()

    if not exist_key_in_dict == "key_name":
        """ RETURN TRUE OR FALSE IF EXIT"""

        exit = DATA_GLOBAL.get(exist_key_in_dict)
        if not exit == False:
            return exist_key_in_dict
        else:
            return False
