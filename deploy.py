import paramiko

def deploy_to_ec2():
    # EC2 instance details
    ec2_host = '3.141.240.128'
    ec2_username = 'edithknaab'
    ec2_key_path = 'csc497_openssh.pem'

    # SSH client setup
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to EC2 instance
        ssh_client.connect(hostname=ec2_host, username=ec2_username, key_filename=ec2_key_path)

        # Commands to execute on EC2 instance
        commands = [
            'cd /path/to/your/react/app',
            'git pull origin master',  # Pull latest changes from your Git repository
            'npm install',             # Install any new dependencies
            'npm run build',           # Build your React application
            'pm2 restart your_app_name' # Restart your application server, assuming you're using pm2
        ]

        # Execute commands on EC2 instance
        for command in commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            # Print command output
            print(stdout.read().decode())
            print(stderr.read().decode())

        print("Deployment completed successfully!")

    except Exception as e:
        print("Error:", e)
    finally:
        # Close SSH connection
        ssh_client.close()

# Trigger deployment
deploy_to_ec2()
