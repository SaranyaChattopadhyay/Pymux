import subprocess

#Configure and check yum configuration on local machine
def yumConfigurationLocal():
    #subprocess.run(['sudo', 'mkdir', '-p', '/dvd'])
    #subprocess.run(['sudo', 'mount', '/dev/cdrom', '/dvd'])
    #subprocess.run(['sudo', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local'])
    #subprocess.run(['sudo', 'chmod', '+x', '/etc/rc.d/rc.local'])
    #subprocess.run(['sudo', 'echo', '"[dvd1]"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #subprocess.run(['sudo', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #subprocess.run(['sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #subprocess.run(['sudo', 'echo', '"[dvd2]"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #subprocess.run(['sudo', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #subprocess.run(['sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo'])
    #output = subprocess.run(['sudo', 'yum', 'repolist'])
    output = subprocess.run(['sudo', 'mkdir', '-p', '/dvd', '&&', 'sudo', 'mount', '/dev/cdrom', '/dvd', '&&', 'sudo', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local', '&&', 'sudo', 'chmod', '+x', '/etc/rc.d/rc.local', '&&', 'sudo', 'echo', '"[dvd1]"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'echo', '"[dvd2]"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'sudo', 'yum', 'repolist'])
    if output.returncode == 0:
        print("Yum configuration successful!")
    else:
        print("Yum configuration unsuccessful!")

#Configure and check yum configuration on remote machine
def yumConfigureRemote(ip):
    output = subprocess.run(['ssh', f'root@{ip}', 'mkdir', '-p', '/dvd', '&&', 'mount', '/dev/cdrom', '/dvd', '&&', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local', '&&', 'chmod', '+x', '/etc/rc.d/rc.local', '&&', 'echo', '"[dvd1]"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'echo', '"[dvd2]"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dvd.repo', '&&', 'yum', 'repolist'])
    if output.returncode == 0:
        print("Yum configuration successful!")
    else:
        print("Yum configuration unsuccessful!")

#Install packages on local machine
def installPackageLocal(package):
    output = subprocess.run(['sudo', 'yum', 'install', f'{package}', '-y'])
    print(output)

#Install packages on remote machine
def installPackageRemote(ip, package):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', f'{package}', '-y'])
    print(output)

#Install and start webserver service on localhost
def webserverLocal():
    output = subprocess.run(['sudo', 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install and start webserver service on remote machine
def webserverRemote(ip):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Create a new user user on local machine
def userCreateLocal(username):
    output = subprocess.run(['sudo', 'useradd', f'{username}'])
    if output.returncode == 0:
        print("User creation successful!")
    else:
        print("User creation unsuccessful!")

#Create a new user user on remote machine
def userCreateRemote(ip, username):
    output = subprocess.run(['ssh', f'root@{ip}', 'useradd', f'{username}'])
    if output.returncode == 0:
        print("User creation successful!")
    else:
        print("User creation unsuccessful!")

#Delete an existing user on local machine
def userDelLocal(username):
    output = subprocess.run(['sudo', 'userdel', '-r', f'{username}'])
    if output.returncode == 0:
        print("User deletion successful!")
    else:
        print("User deletion unsuccessful!")

#Delete an existing user user on remote machine
def userDelRemote(ip, username):
    output = subprocess.run(['ssh', f'root@{ip}', 'userdel', '-r', f'{username}'])
    if output.returncode == 0:
        print("User deletion successful!")
    else:
        print("User deletion unsuccessful!")

#Create new folder on local machine
def createFolderLocal(folder_path):
    output = subprocess.run(['sudo', 'mkdir', '-p', f'{folder_path}'])
    if output.returncode == 0:
        print("Folder created successfully!")
    else:
        print("Folder creation unsuccessful!")

#Create new folder on remote machine
def createFolderRemote(ip, folder_path):
    output = subprocess.run(['ssh', f'root@{ip}', 'mkdir', '-p', f'{folder_path}'])
    if output.returncode == 0:
        print("Folder created successfully!")
    else:
        print("Folder creation unsuccessful!")

#Configure docker on local machine
def confDockerLocal():
    subprocess.run(['sudo', 'echo', '"[docker]"', '>>', '/etc/yum.repos.d/dockerRepo.repo'])
    subprocess.run(['sudo', 'echo', '"baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/"', '>>', '/etc/yum.repos.d/dockerRepo.repo'])
    subprocess.run(['sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dockerRepo.repo'])
    subprocess.run(['sudo', 'yum', 'install', 'docker-ce', '--nobest', '-y'])
    output = subprocess.run(['sudo', 'systemctl', 'start', 'docker'])
    if output.returncode == 0:
        print("Docker configuration successful!")
    else:
        print("Docker configuration unsuccessful!")

#Configure docker on remote machine
def confDockerRemote(ip):
    output = subprocess.run(['ssh', f'root@{ip}', 'echo', '"[docker]"', '>>', '/etc/yum.repos.d/dockerRepo.repo', '&&', 'echo', '"baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/"', '>>', '/etc/yum.repos.d/dockerRepo.repo', '&&', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repos.d/dockerRepo.repo', '&&', 'yum', 'install', 'docker-ce', '--nobest', '-y', '&&', 'systemctl', 'start', 'docker'])
    if output.returncode == 0:
        print("Docker configuration successful!")
    else:
        print("Docker configuration unsuccessful!")

#Run docker commands on local machine
def runDockerLocal(command):
    output = subprocess.getoutput(command)
    print(output)

#Run docker commands on remote machine
def runDockerRemote(ip, command):
    output = subprocess.getoutput(['ssh', f'root@{ip}', f'{command}'])
    print(output)

#Create physical volume on local machine
def createPVLocal(disk_name):
    output = subprocess.run(['sudo', 'pvcreate', f'{disk_name}'])
    if output.returncode == 0:
        print("Physical volume successfully created!")
    else:
        print("Physical volume creation failed!")

#Create physical volume on remote machine
def createPVRemote(ip, disk_name):
    output = subprocess.run(['ssh', f'root@{ip}', 'pvcreate', f'{disk_name}'])
    if output.returncode == 0:
        print("Physical volume successfully created!")
    else:
        print("Physical volume creation failed!")

#Create volume group on local machine
def createVGLocal(vgName, pv1, pv2):
    output = subprocess.run(['sudo', 'vgcreate', f'{vgName}', f'{pv1}', f'{pv2}'])
    if output.returncode == 0:
        print("Volume group successfully created")
    else:
        print("Volume group creation failed")

#Create volume group on remote machine
def createVGRemote(ip, vgName, pv1, pv2):
    output = subprocess.run(['ssh', f'root@{ip}', 'vgcreate', f'{vgName}', f'{pv1}', f'{pv2}'])
    if output.returncode == 0:
        print("Volume group successfully created")
    else:
        print("Volume group creation failed")

#Create logical volume on local machine
def createLVLocal(lvName, vgName, lvSize):
    output = subprocess.run(['sudo', 'lvcreate', '--size', f'{lvSize}', '--name', f'{lvName}', f'{vgName}'])
    if output.returncode == 0:
        print("Logical volume successfully created")
    else:
        print("Logical volume creation failed")

#Create logical volume on remote machine
def createLVRemote(ip, lvName, vgName, lvSize):
    output = subprocess.run(['ssh', f'root@{ip}', 'lvcreate', '--size', f'{lvSize}', '--name', f'{lvName}', f'{vgName}'])
    if output.returncode == 0:
        print("Logical volume successfully created")
    else:
        print("Logical volume creation failed")

if __name__ == "__main__":
    #yumConfigurationLocal()
    #yumConfigureRemote("192.168.29.22")
    #installPackageLocal()
    #installPackageRemote("192.168.29.22", "git")
    #webserverLocal()
    #webserverRemote("192.168.29.22")
    #userCreateLocal("saptarsi")
    #userCreateRemote("saptarsi")
    #userDelLocal("saptarsi")
    #userDelRemote("saptarsi")
    #createFolderLocal()
    #createFolderRemote()
    #confDockerLocal()
    #confDockerRemote("192.168.29.22")
    #runDockerLocal()
    #runDockerRemote()
    pass


