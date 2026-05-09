from abc import ABC, abstractmethod


class IslamicContract(ABC):
    """
    Abstract base class for Shariah-compliant financial contracts.
    """

    def __init__(self, contract_name):
        self.contract_name = contract_name

    @abstractmethod
    def contract_value(self):
        pass

    @abstractmethod
    def summary(self):
        pass


class Murabaha(IslamicContract):
    """
    Murabaha: cost-plus sale.
    """

    def __init__(self, asset_name, cost_price, profit_rate):
        super().__init__("Murabaha")
        if cost_price <= 0:
            raise ValueError("Cost price must be positive")
        if profit_rate < 0:
            raise ValueError("Profit rate cannot be negative")

        self.asset_name = asset_name
        self.cost_price = cost_price
        self.profit_rate = profit_rate

    @property
    def profit_amount(self):
        return self.cost_price * self.profit_rate / 100

    def contract_value(self):
        return self.cost_price + self.profit_amount

    def summary(self):
        return (
            f"{self.contract_name} Contract | Asset: {self.asset_name} | "
            f"Cost Price: {self.cost_price} | Profit Rate: {self.profit_rate}% | "
            f"Selling Price: {self.contract_value()}"
        )


class Ijara(IslamicContract):
    """
    Ijara: leasing contract.
    """

    def __init__(self, asset_name, monthly_rent, months):
        super().__init__("Ijara")
        if monthly_rent <= 0:
            raise ValueError("Monthly rent must be positive")
        if months <= 0:
            raise ValueError("Months must be positive")

        self.asset_name = asset_name
        self.monthly_rent = monthly_rent
        self.months = months

    def contract_value(self):
        return self.monthly_rent * self.months

    def summary(self):
        return (
            f"{self.contract_name} Contract | Asset: {self.asset_name} | "
            f"Monthly Rent: {self.monthly_rent} | Duration: {self.months} months | "
            f"Total Rent: {self.contract_value()}"
        )


class Mudarabah(IslamicContract):
    """
    Mudarabah: profit-sharing partnership.
    """

    def __init__(self, capital, total_profit, investor_ratio):
        super().__init__("Mudarabah")
        if capital <= 0:
            raise ValueError("Capital must be positive")
        if total_profit < 0:
            raise ValueError("Total profit cannot be negative")
        if not (0 <= investor_ratio <= 1):
            raise ValueError("Investor ratio must be between 0 and 1")

        self.capital = capital
        self.total_profit = total_profit
        self.investor_ratio = investor_ratio

    @property
    def investor_share(self):
        return self.total_profit * self.investor_ratio

    @property
    def entrepreneur_share(self):
        return self.total_profit - self.investor_share

    def contract_value(self):
        return self.capital + self.total_profit

    def summary(self):
        return (
            f"{self.contract_name} Contract | Capital: {self.capital} | "
            f"Total Profit: {self.total_profit} | Investor Share: {self.investor_share} | "
            f"Entrepreneur Share: {self.entrepreneur_share}"
        )


# Demo
if __name__ == "__main__":
    contracts = [
        Murabaha("Laptop", 100000, 10),
        Ijara("Office Equipment", 15000, 12),
        Mudarabah(500000, 80000, 0.6)
    ]

    for contract in contracts:
        print(contract.summary())
