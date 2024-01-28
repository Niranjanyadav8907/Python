
# Inheritance******Gate Smashers*******

## Inheritance - Inheritance allows us to define a class that inherits 
#all the methods and properties from another class

class OOTsubscription:
    def __init__(self, subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.payment=total_payment
    def subscribe(self):
        print(f"subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"subscriber with {self.id} id unsubscribed to the {self.plan}plan")


#example
netflix=OOTsubscription(121212,"monthly",100)
print(netflix.plan)
print(netflix.subscribe())


# subclass ki child class inheritance execute

#subclass
class OOTsubscription:
    def __init__(self, subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.payment=total_payment
    def subscribe(self):
        print(f"subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"subscriber with {self.id} id unsubscribed to the {self.plan}plan")

#child class 
class premiumscription(OOTsubscription):
    def __init__(self, subscription_id, plan, total_payment,screens):
        self.id = subscription_id
        self.plan = plan
        self.payment=total_payment
        self.max_screans = screens # inherit new class
    def subscribe(self):
        print(f"subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"subscriber with {self.id} id unsubscribed to the {self.plan}plan")

    def set_max_screen(self, screens):
        self.max_screans = screens
        print(f"maximum screen set to {self.max_screans} in  premium plan")


# Example usage
    
netflix = premiumscription("1234567", "monthly", 1,1200)
print(netflix.subscribe())
print(netflix.set_max_screen(4))



# inheritance super class

class OOTsubscription:
    def __init__(self, subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.payment=total_payment
    def subscribe(self):
        print(f"subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"subscriber with {self.id} id unsubscribed to the {self.plan}plan")

#superclass
class premiumscription(OOTsubscription):
    def __init__(self, subscription_id, plan, total_payment,screens):
        super().__init__(subscription_id, plan, total_payment)
        self.max_screans =screens
        
    def set_max_screen(self, screens):
        self.max_screans = screens
        print(f"maximum screen set to {self.max_screans} in  premium plan")

    
# example
        
netflix = premiumscription("1234567", "monthly", 1,1200)
print(netflix.subscribe())
print(netflix.set_max_screen(4))

        













        
     

