"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_change_staging_from_folder_requested.py

This file defines the DbusChangeStagingFromFolderRequested class.

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
from pythoneda.shared.artifact_changes.events.change_staging_from_folder_requested import ChangeStagingFromFolderRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusChangeStagingFromFolderRequested(ServiceInterface):
    """
    D-Bus interface for ChangeStagingFromFolderRequested

    Class name: DbusChangeStagingFromFolderRequested

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingFromFolderRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingFromFolderRequested.
        """
        super().__init__("pythonedaartifactchanges_ChangeStagingFromFolderRequested")

    @signal()
    def ChangeStagingFromFolderRequested(self, repositoryFolder: "s"):
        """
        Defines the ChangeStagingFromFolderRequested d-bus signal.
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
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
    def transform_ChangeStagingFromFolderRequested(
        self, event: ChangeStagingFromFolderRequested
    ) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.change_staging_from_folder_requested.ChangeStagingFromFolderRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.repository_folder,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def signature_for_ChangeStagingFromFolderRequested(cls, event: ChangeStagingFromFolderRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.change_staging_from_folder_requested.ChangeStagingFromFolderRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse_pythonedaartifactchanges_ChangeStagingFromFolderRequested(
        cls, message: Message
    ) -> ChangeStagingFromFolderRequested:
        """
        Parses given d-bus message containing a ChangeStagingFromFolderRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingFromFolderRequested event.
        :rtype: pythonedaartifacteventchanges.change_staging_from_folder_requested.ChangeStagingFromFolderRequested
        """
        repository_folder, event_id, prev_event_id = message.body
        return ChangeStagingFromFolderRequested(
            repository_folder, None, event_id, json.loads(prev_event_id)
        )
