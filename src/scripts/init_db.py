import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_session
from src.models import User, Role, Permission, Profile
from passlib.context import CryptContext

# Contexte de hachage pour sécuriser le mot de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_initial_data():
    async with async_session() as session:
        async with session.begin():
            # Vérification de l'existence des permissions de base
            manage_role_permission_result = await session.execute(
                select(Permission).filter_by(name="manage_role")
            )
            manage_permission_permission_result = await session.execute(
                select(Permission).filter_by(name="manage_permission")
            )

            manage_role = manage_role_permission_result.scalar()
            manage_permission = manage_permission_permission_result.scalar()

            # Création des permissions si elles n'existent pas
            if not manage_role:
                manage_role = Permission(name="manage_role")
                session.add(manage_role)

            if not manage_permission:
                manage_permission = Permission(name="manage_permission")
                session.add(manage_permission)

            # Vérification et création du rôle admin
            admin_role_result = await session.execute(
                select(Role).filter_by(name="admin")
            )
            admin_role = admin_role_result.scalar()

            if not admin_role:
                admin_role = Role(name="admin")
                admin_role.permissions = [manage_role, manage_permission]
                session.add(admin_role)
                await session.flush()

            # Vérification et création du rôle utilisateur par défaut
            user_role_result = await session.execute(
                select(Role).filter_by(name="user")
            )
            user_role = user_role_result.scalar()

            if not user_role:
                user_role = Role(name="user")
                session.add(user_role)
                await session.flush()

            # Vérification et création de l'utilisateur admin
            admin_user_result = await session.execute(
                select(User).filter_by(email="admin@example.com")
            )
            admin_user = admin_user_result.scalar()

            if not admin_user:
                hashed_password = pwd_context.hash("admin")  # Change ce mot de passe par sécurité après l'init
                admin_user = User(
                    email="admin@example.com",
                    password=hashed_password,
                    roles=[admin_role, user_role]  # Ajouter plusieurs rôles
                )
                session.add(admin_user)

                # Création d'un profil pour l'utilisateur admin
                admin_profile = Profile(
                    firstname="Admin",
                    name="User",
                    age=30,
                    weight=70,
                    height=170,
                    user=admin_user
                )
                session.add(admin_profile)

            await session.commit()
