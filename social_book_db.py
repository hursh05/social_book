import os
import django
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Set up Django settings and environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_book.settings')
django.setup()

# Define the SQLAlchemy Base
Base = declarative_base()

# Define the User model in SQLAlchemy
class User(Base):
    __tablename__ = 'users'  # Table name in social_book database

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)  # Assuming password is already hashed

# SQLAlchemy engine and session setup
DATABASE_URL = "postgresql://myuser:password@localhost:5432/social_book"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Function to transfer users from Django to SQLAlchemy
def transfer_users_to_social_book():
    # Get the custom user model from Django
    CustomUser = get_user_model()

    # Fetch all users from Django
    users = CustomUser.objects.all()

    # Create a session for SQLAlchemy
    session = Session()

    # Add each Django user to the social_book database
    for user in users:
        password = make_password(user.password)  # Hash the password before saving
        new_user = User(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=password  # Store the hashed password
        )
        session.add(new_user)

    # Commit the transaction to the social_book database
    session.commit()
    session.close()

# Run the user transfer
if __name__ == "__main__":
    transfer_users_to_social_book()
