"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_staged_changes_committed.py

This file defines the DbusStagedChangesCommitted class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/event-infrastructure

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
from pythoneda.shared.artifact_changes import Change
from pythoneda.shared.artifact_changes.events import StagedChangesCommitted
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusStagedChangesCommitted(ServiceInterface):
    """
    D-Bus interface for StagedChangesCommitted

    Class name: DbusStagedChangesCommitted

    Responsibilities:
        - Define the d-bus interface for the StagedChangesCommitted event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusStagedChangesCommitted.
        """
        super().__init__("pythonedaartifactchanges_StagedChangesCommitted")

    @signal()
    def StagedChangesCommitted(self, change: "s"):
        """
        Defines the StagedChangesCommitted d-bus signal.
        :param change: The change.
        :type change: str
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
    def transform_StagedChangesCommitted(
        self, event: StagedChangesCommitted
    ) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.change_staging_requested.StagedChangesCommitted
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.message,
            event.repository_url,
            event.branch,
            event.repository_folder,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def signature_for_StagedChangesCommitted(
        cls, event: StagedChangesCommitted
    ) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.change_staging_requested.StagedChangesCommitted
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse_pythonedaartifactchanges_StagedChangesCommitted(
        cls, message: Message
    ) -> StagedChangesCommitted:
        """
        Parses given d-bus message containing a StagedChangesCommitted event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The StagedChangesCommitted event.
        :rtype: pythonedaartifacteventchanges.change_staging_requested.StagedChangesCommitted
        """
        (
            msg,
            repository_url,
            branch,
            repository_folder,
            event_id,
            prev_event_ids,
        ) = message.body
        return StagedChangesCommitted(
            msg,
            repository_url,
            branch,
            repository_folder,
            None,
            event_id,
            json.loads(prev_event_ids),
        )
