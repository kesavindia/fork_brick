import datetime

class PurchaseManager:
    """
    Manages purchase-related operations, including configurations, cost calculations,
    and bill generation.
    """

    def __init__(self, configurations):
        """
        Initializes the PurchaseManager with configurations.

        Args:
            configurations (dict): Dictionary containing configuration values.
        """
        self.configurations = configurations

    def update_configuration(self, key, value):
        """
        Updates a configuration value.

        Args:
            key (str): The configuration key to update.
            value: The new value for the configuration.

        Returns:
            bool: True if successful, False otherwise.
        """

        if key in self.configurations:
            self.configurations[key] = value
            return True
        else:
            return False

    def get_raw_material_cost(self, raw_material_id):
        """
        Retrieves the cost of a raw material based on its ID.

        This is a placeholder function. You need to implement the logic to access your
        data source (e.g., database, file) and retrieve the actual cost based on the ID.

        Args:
            raw_material_id (int): The ID of the raw material.

        Returns:
            float: The cost of the raw material.
        """

        # Replace this with your actual implementation to retrieve cost from data source
        return raw_material_id * 1.5  # Placeholder value

    def calculate_labor_cost(self, joining_date):
        """
        Calculates the labor cost based on joining date and attendance.

        Args:
            joining_date (str): The date of joining in YYYY-MM-DD format.

        Returns:
            float: The calculated labor cost.
        """

        # Convert joining date to a comparable format
        joining_date_obj = datetime.datetime.strptime(joining_date, "%Y-%m-%d")

        # Determine monthly wage based on joining date
        monthly_wage = 15000 if joining_date_obj < datetime.datetime(2024, 1, 1) else 12000

        # Access daily wage from configurations
        daily_wage = self.configurations["daily_wage"]

        # Replace this with your actual implementation to calculate labor cost based on attendance and wage rates
        labor_cost_per_day = int(input("Enter labour cost per day: "))
        labor_cost = 26 * labor_cost_per_day + monthly_wage
        return labor_cost

    def calculate_profit_share(self, investment_share):
        """
        Calculates the profit share based on investment distribution and raw material cost.

        Args:
            investment_share (float): The investor's percentage of share.

        Returns:
            float: The calculated profit share.
        """

        raw_material_cost = self.get_raw_material_cost()
        profit_share = raw_material_cost * investment_share
        return profit_share

    def generate_purchase_bill(self, raw_material_id, quantity, cost_per_kg):
        """
        Generates a purchase bill for raw materials.

        Args:
            raw_material_id (int): The ID of the raw material.
            quantity (int): The quantity of raw materials purchased.
            cost_per_kg (float): The cost per kilogram of the raw material.

        Returns:
            dict: The purchase bill details.
        """

        cost_of_raw_material = raw_material_id * 1.5 * quantity * cost_per_kg
        return {
            "raw_material_id": raw_material_id,
            "quantity": quantity,
            "cost_per_kg": cost_per_kg,
            "total_cost": cost_of_raw_material
        }


# Example usage
configurations = {
    "investment_distribution": [0.5, 0.3, 0.2],  # Percentages for investors
    "transportation_charge": 10,  # Per kilometer
    "billing_criteria": {
        "raw_material_weight": 0.6,
        "labor_cost_weight": 0.2,
        "profit_share_criteria": [
            {"min_investment": 10000}
    ]
    }}
