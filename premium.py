class Premium:
    """Creates a premium for a vessel for a cover type"""
    def __init__(self):
        self.premiums = []

    # Calculate the inception premium on a vessel
    def calculate_inception_premium(self, policy):
        for cover in policy.covers:
            for asset in policy.assets:
                self.premiums.append(round((cover.rate/100/365)*asset.value*policy.days, 2))
