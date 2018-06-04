def get_latest_file(devicename,bgp_ip,role):
    import glob
    import os
    try:
        list_of_files = glob.glob('./*.txt') # * means all if need specific format
        #we can use regex above string to get lastest file from pool of interested files and format.
        latest_file = max(list_of_files, key=os.path.getctime)
    except:
        latest_file = None
    return latest_file
