"""
  Estructura que contiene la información a guardar en una ``entry`` de un Map
"""

def new_map_entry(key, value):
    """ Retorna una pareja llave valor para ser guardada en un Map

        :param key: Llave de la pareja
        :type key: any
        :param value: Valor de la pareja
        :type value: any

        :return: Una entrada con la pareja llave-valor
        :rtype: map_entry
    """
    entry = {'key': key, 'value': value}
    return entry


def set_key(my_entry, key):
    """ Asigna un valor nuevo a la ``key`` del entry recibido como parámetro

        :param my_entry: La pareja llave-valor
        :type my_entry: map_entry
        :param key: La nueva llave
        :type key: any

        :return: La pareja modificada
        :rtype: map_entry
    """
    my_entry['key'] = key
    return my_entry


def set_value(my_entry, value):
    """Asigna un valor nuevo al ``value`` del entry recibido como parámetro

        :param my_entry: La pareja llave-valor
        :type my_entry: map_entry
        :param value: El nuevo value
        :type value: any

        :return: La pareja modificada
        :rtype: map_entry
    """
    my_entry['value'] = value
    return my_entry


def get_key(my_entry):
    """ 
    Retorna la llave de la entry recibida como parámetro

    :param my_entry: La pareja llave-valor
    :type my_entry: map_entry

    :return: La llave de la pareja
    :rtype: any
    """
    return my_entry['key']


def get_value(my_entry):
    """
    Retorna el valor de la entry recibida como parámetro

    :param my_entry: La pareja llave-valor
    :type my_entry: map_entry
    
    :return: El valor de la pareja
    :rtype: any
    """
    return my_entry['value']
