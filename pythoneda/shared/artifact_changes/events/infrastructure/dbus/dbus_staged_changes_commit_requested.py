"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_staged_changes_commit_requested.py

This file defines the DbusStagedChangesCommitRequested class.

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
from pythoneda.shared.artifact_changes import Change
from pythoneda.shared.artifact_changes.events.staged_changes_commit_requested import StagedChangesCommitRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusStagedChangesCommitRequested(ServiceInterface):
    """
    D-Bus interface for StagedChangesCommitRequested

    Class name: DbusStagedChangesCommitRequested

    Responsibilities:
        - Define the d-bus interface for the StagedChangesCommitRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusStagedChangesCommitRequested.
        """
        super().__init__("pythonedaartifactchanges_StagedChangesCommitRequested")

    @signal()
    def StagedChangesCommitRequested(self, change: "s"):
        """
        Defines the StagedChangesCommitRequested d-bus signal.
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
    def transform_StagedChangesCommitRequested(
        self, event: StagedChangesCommitRequested
    ) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.staged_changes_commit_requested.StagedChangesCommitRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [event.message, event.repository_url, event.branch, event.repository_folder, event.id, json.dumps(event.previous_event_ids)]

    @classmethod
    def signature_for_StagedChangesCommitRequested(cls, event: StagedChangesCommitRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.staged_changes_commit_requested.StagedChangesCommitRequested
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse_pythonedaartifactchanges_StagedChangesCommitRequested(
        cls, message: Message
    ) -> StagedChangesCommitRequested:
        """
        Parses given d-bus message containing a StagedChangesCommitRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The StagedChangesCommitRequested event.
        :rtype: pythonedaartifacteventchanges.staged_changes_commit_requested.StagedChangesCommitRequested
        """
        msg, repository_url, branch, repository_folder, event_id, prev_event_ids = message.body
        return StagedChangesCommitRequested(
            msg, repository_url, branch, repository_folder, None, event_id, json.loads(prev_event_ids)
        )
