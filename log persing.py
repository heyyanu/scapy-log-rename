with open("apache_logs.txt","r") as f:
    for line in f:
        parts =line.split()

        ip= parts[0]
        Timedate =parts[3]+" "+parts[4]
        status_code= parts[8]

        if status_code =="200":
          print(f"IP: {ip}, Timedate: {Timedate}, Status: {status_code}")






