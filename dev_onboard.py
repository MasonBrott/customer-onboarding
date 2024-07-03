import argparse
import json
import subprocess

# Setting up arguments for customer, domain, and realm
parser = argparse.ArgumentParser(
    prog="Add new client to CMMC Space",
    description="Automate the customer onboarding stage"
)

parser.add_argument("-c", "--customer",
                    action="store",
                    help="Name of the customer")

parser.add_argument("-d", "--domain",
                    action="store",
                    help="Domain of the customer (customer.cmmc.space)")

# Realm will default to 0 if not given a value
parser.add_argument("-r", "--realm",
                    nargs='?',
                    const= 0,
                    default= 0,
                    action="store",
                    help="Which realm will the customer be added to (default to 0)")

args = parser.parse_args()
customer_name = args.customer
domain = args.domain
realm_number = str(args.realm)

# Open the tfvars file as a JSON file to parse
with open('dev.tfvars.json', 'r') as file:
    tfvars = json.load(file)


realm = tfvars['realms'][realm_number]
customers = realm['customers']

# Add the new customer with their domain to the realm specified
customers[customer_name] = {'domain': domain}

# Overwrite the previous tfvars file with the new customer
with open('dev.tfvars.json', 'w') as file:
    json.dump(tfvars, file, indent=2)


def run_git_command(command, message=None):
    try:
        # Set user information for this specific command
        subprocess.run(['git', 'config', 'user.email', '"mbrott@atxdefense.com"'], check=True)
        subprocess.run(['git', 'config', 'user.name', '"Masonbrott"'], check=True)

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
        if message:
            print(message)
    except subprocess.CalledProcessError as e:
        print(f"Error running Git command '{command}':\n{e.stderr}")
        raise SystemExit(1)
    
# Make sure that the local git repo is up to date so there are no conflicts
run_git_command(['git', 'pull'], "Local repository is up to date")

# Git Interactions (with explicit user configuration before each command)
run_git_command('git', 'checkout', '-b', f'{customer_name} onboarding')
run_git_command(['git', 'commit', '-m', f'Adding {customer_name} to CMMC Space'])
run_git_command(['git', 'push'], f'Added {customer_name} to cmmc-vdi-images')

