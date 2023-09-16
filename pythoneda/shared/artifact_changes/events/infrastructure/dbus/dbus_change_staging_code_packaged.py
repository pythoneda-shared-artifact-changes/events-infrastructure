"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_change_staging_code_packaged.py

This file defines the DbusChangeStagingCodePackaged class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda import BaseObject
from pythoneda.shared.code_requests.jupyter import JupyterlabNixFlake
from pythoneda.shared.artifact_changes.events import ChangeStagingCodePackaged
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusChangeStagingCodePackaged(BaseObject, ServiceInterface):
    """
    D-Bus interface for ChangeStagingCodePackaged

    Class name: DbusChangeStagingCodePackaged

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodePackaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodePackaged.
        """
        super().__init__(
            "Pythoneda_Shared_artifact_changes_Events_ChangeStagingCodePackaged"
        )

    @signal()
    def ChangeStagingCodePackaged(self, nixFlake: "s"):
        """
        Defines the ChangeStagingPackaged d-bus signal.
        :param nixFlake: The Nix .
        :type nixFlake: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(self, event: ChangeStagingCodePackaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact_changes.events.ChangeStagingCodePackaged
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.nix_flake.to_json(),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodePackaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact_changes.events.ChangeStagingCodePackaged
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodePackaged:
        """
        Parses given d-bus message containing a ChangeStagingCodePackaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingPackaged event.
        :rtype: pythoneda.shared.artifact_changes.events.ChangeStagingCodePackaged
        """
        nix_flake_json, event_id, prev_event_ids = message.body
        return ChangeStagingCodePackaged(
            JupyterlabNixFlake.from_json(nix_flake_json),
            None,
            event_id,
            json.loads(prev_event_ids),
        )
