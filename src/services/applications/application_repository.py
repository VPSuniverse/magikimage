import json
import os
from typing import List, Dict, Optional

class Application:
    def __init__(self, app_id: str, name: str, packages: Dict[str, str], description: str = ""):
        self.id = app_id
        self.name = name
        self.packages = packages
        self.description = description

    def get_package_name_for_manager(self, manager_type: str) -> Optional[str]:
        return self.packages.get(manager_type.lower())

class ApplicationRepository:
    def __init__(self, config_file_path: str = "src/config/applications.json"):
        # Construir la ruta absoluta al archivo de configuración
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.config_path = os.path.join(base_dir, config_file_path.replace("src/", "", 1))
        self.applications: List[Application] = self._load_applications()

    def _load_applications(self) -> List[Application]:
        apps = []
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for app_data in data:
                    apps.append(Application(
                        app_id=app_data.get("id"),
                        name=app_data.get("name"),
                        packages=app_data.get("packages"),
                        description=app_data.get("description", "")
                    ))
        except FileNotFoundError:
            print(f"Error: Application config file not found at {self.config_path}")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {self.config_path}")
        return apps

    def get_all_applications(self) -> List[Application]:
        return self.applications

    def find_application_by_id(self, app_id: str) -> Optional[Application]:
        for app in self.applications:
            if app.id == app_id:
                return app
        return None