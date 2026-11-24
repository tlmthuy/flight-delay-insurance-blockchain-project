"""Prototype nghiệp vụ trong bộ nhớ, dùng chuẩn bị trao đổi với giảng viên.

Chạy bằng python scripts/business_flow_demo.py.
Các giá trị tiền là số nguyên minh họa. Chưa có blockchain hoặc giao dịch ví.
"""

from dataclasses import dataclass
import sys


@dataclass
class Policy:
    owner: str
    payout: int
    status: str = "Active"


class InsuranceDemo:
    def __init__(self):
        self.balance = 100
        self.reserved = 0
        self.policies = {}

    def buy(self, policy_id, owner, premium, payout):
        if policy_id in self.policies:
            raise ValueError("Policy đã tồn tại")
        if not owner or premium <= 0 or payout <= 0:
            raise ValueError("Thông tin hoặc số tiền không hợp lệ")
        if self.balance + premium < self.reserved + payout:
            raise ValueError("Quỹ không đủ để cam kết bồi thường")
        self.policies[policy_id] = Policy(owner=owner, payout=payout)
        self.balance += premium
        self.reserved += payout

    def settle(self, policy_id, caller, delay_minutes=0, cancelled=False):
        if caller != "oracle":
            raise ValueError("Người gọi không có quyền oracle")
        policy = self.policies[policy_id]
        if policy.status != "Active":
            raise ValueError("Policy đã được giải quyết")
        if cancelled or delay_minutes >= 120:
            policy.status = "Claimable"
        else:
            policy.status = "Closed"
            self.reserved -= policy.payout

    def claim(self, policy_id, caller):
        policy = self.policies[policy_id]
        if caller != policy.owner:
            raise ValueError("Người gọi không phải người nhận")
        if policy.status != "Claimable":
            raise ValueError("Policy chưa đủ điều kiện hoặc đã nhận tiền")
        policy.status = "Paid"
        self.balance -= policy.payout
        self.reserved -= policy.payout


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("PROTOTYPE MÔ PHỎNG NGHIỆP VỤ · TIỀN MINH HỌA")
    demo = InsuranceDemo()
    for policy_id, delay, cancelled in (
        ("ON_TIME", 0, False),
        ("DELAY_119", 119, False),
        ("DELAY_120", 120, False),
        ("CANCELLED", 0, True),
    ):
        demo.buy(policy_id, "passenger", premium=2, payout=10)
        demo.settle(policy_id, "oracle", delay, cancelled)
        policy = demo.policies[policy_id]
        print(f"{policy_id}: {policy.status}")
        if policy.status == "Claimable":
            demo.claim(policy_id, "passenger")
            print(f"  Nhận bồi thường: {policy.status}")

    for description, action in (
        ("Claim lần hai", lambda: demo.claim("DELAY_120", "passenger")),
        ("Oracle trái quyền", lambda: demo.settle("ON_TIME", "passenger")),
        ("Quỹ thiếu vốn", lambda: demo.buy("TOO_LARGE", "passenger", 2, 1000)),
    ):
        try:
            action()
        except ValueError as error:
            print(f"{description}: từ chối ({error})")
        else:
            raise AssertionError(f"Kịch bản phải bị từ chối: {description}")

    assert demo.policies["DELAY_119"].status == "Closed"
    assert demo.policies["DELAY_120"].status == "Paid"
    assert demo.policies["CANCELLED"].status == "Paid"
    assert demo.balance == 88 and demo.reserved == 0
    print(f"Quỹ cuối: {demo.balance}; khoản còn cam kết: {demo.reserved}")


if __name__ == "__main__":
    main()
