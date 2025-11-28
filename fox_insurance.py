from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
from typing import List
from dataclasses import dataclass

class CoverageType(Enum):
    LIABILITY = "liability"
    PROPERTY = "property"
    WORKERS_COMP = "workers_compensation"
    CYBER = "cyber"

@dataclass
class Coverage:
    type: CoverageType
    limit: float
    deductible: float
    premium: float

@dataclass
class Policy:
    policy_id: str
    company_name: str
    start_date: datetime
    end_date: datetime
    coverages: List[Coverage]
    status: str = "active"
    
    def calculate_total_premium(self) -> float:
        return sum(coverage.premium for coverage in self.coverages)
    
    def is_expired(self) -> bool:
        return datetime.now() > self.end_date

class InsuranceManager:
    def __init__(self):
        self.policies: List[Policy] = []
    
    def create_policy(self, company_name: str, coverages: List[Coverage]) -> Policy:
        policy = Policy(
            policy_id=f"POL-{len(self.policies)+1}",
            company_name=company_name,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=365),
            coverages=coverages
        )
        self.policies.append(policy)
        return policy
    
    def get_policy(self, policy_id: str) -> Policy:
        return next((p for p in self.policies if p.policy_id == policy_id), None)
    
    def renew_policy(self, policy_id: str) -> Policy:
        policy = self.get_policy(policy_id)
        if policy:
            policy.end_date = datetime.now() + timedelta(days=365)
            policy.status = "active"
        return policy