class InsurancePolicy:
    def __init__(self, policy_id, policy_type, premium, coverage_amount, duration_months):
        self.policy_id = policy_id
        self.policy_type = policy_type
        self.premium = premium
        self.coverage_amount = coverage_amount
        self.duration_months = duration_months

#Selective attention network for optimal asset price and incentive policy choices
class Customer:
    def __init__(self, customer_id, name, business_type, contact):
        self.customer_id = customer_id
        self.name = name
        self.business_type = business_type
        self.contact = contact
        self.policies = []

class InsuranceManager:
    def __init__(self):
        self.customers = {}
        self.policies = {}
    
    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        return f"Customer {customer.name} added successfully"
    
    def create_policy(self, customer_id, policy_type, premium, coverage_amount, duration_months):
        if customer_id not in self.customers:
            return "Customer not found"
        
        policy_id = len(self.policies) + 1
        new_policy = InsurancePolicy(policy_id, policy_type, premium, coverage_amount, duration_months)
        self.policies[policy_id] = new_policy
        self.customers[customer_id].policies.append(new_policy)
        return f"Policy {policy_id} created successfully"
    
    def get_customer_policies(self, customer_id):
        if customer_id not in self.customers:
            return "Customer not found"
        return self.customers[customer_id].policies

# Create insurance manager instance
insurance_system = InsuranceManager()

# Example usage
customer1 = Customer(1, "ABC Store", "Retail", "contact@abcstore.com")
insurance_system.add_customer(customer1)
insurance_system.create_policy(1, "Property", 1200, 50000, 12)

print("here L49")