def capital_country(capital, country, population=''):
    if population:
        whole_name = f"{capital}, {country} - population {population}"
    else: 
        whole_name = f"{capital}, {country}"
    return whole_name.title()