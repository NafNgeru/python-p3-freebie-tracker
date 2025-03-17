#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Seed data
company1 = Company(name="Microsoft", founding_year=1994)
company2 = Company(name="IBM", founding_year=1987)

dev1 = Dev(name="Naftaly")
dev2 = Dev(name="Maureen")

freebie1 = Freebie(item_name="Gift-card", value=10, dev_id=dev1.id, company_id=company1.id)
freebie2 = Freebie(item_name="Trophy", value=2, dev_id=dev2.id, company_id=company2.id)
freebie3 = Freebie(item_name="Mug", value=15, dev_id=dev1.id, company_id=company2.id)


# Add to session
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("Congratulations!! Database seeded successfully!")