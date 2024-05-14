import argparse

parser = argparse.ArgumentParser(
    prog="Customer Onboarding",
    description="Automate more of the onboarding of new customers"
)

parser.add_argument("-s", "--customer",
                    action="store",
                    help="Name of the customer")
parser.add_argument("-d", "--domain",
                    action="store",
                    help="Domain of the customer (something.cmmc.space)")

args = parser.parse_args()

customer = args.customer
domain = args.domain


