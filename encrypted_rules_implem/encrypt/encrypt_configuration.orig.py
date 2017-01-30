# Copy this file to configuration.py and complete the token
# centralize all configurations :

class Configuration:
    # log
    log_path = '/var/log/squid3/access.log'

    # redis
    redis_host = 'localhost'
    redis_port = 6379
    redis_db = 0
    
    # misp
    misp_token = ''
    misp_email = ''

    # misp Web Api
    misp_url = 'https://misppriv.circl.lu/'

    # misp mysql database
    user = ''
    password = ''
    host = ''
    dbname = 'misp'
    
    # rules
    rule_location = 'rules'
