"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_staged_changes_commit_code_requested.py

This file defines the DbusStagedChangesCommitCodeRequested class.

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
from pythoneda.shared.artifact_changes import Change
from pythoneda.shared.artifact_changes.events import StagedChangesCommitCodeRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusStagedChangesCommitCodeRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for StagedChangesCommitCodeRequested

    Class name: DbusStagedChangesCommitCodeRequested

    Responsibilities:
        - Define the d-bus interface for the StagedChangesCommitCodeRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusStagedChangesCommitCodeRequested.
        """
        super().__init__("Pythoneda_Shared_artifact_changes_Events_StagedChangesCommitCodeRequested")

    @signal()
    def StagedChangesCommitCodeRequested(self, change: "s"):
        """
        Defines the StagedChangesCommitCodeRequested d-bus signal.
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
    def transform(
        self, event: StagedChangesCommitCodeRequested
    ) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact_changes.events.StagedChangesCommitCodeRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [event.message, event.repository_url, event.branch, event.repository_folder, event.id, json.dumps(event.previous_event_ids)]

    @classmethod
    def signature(cls, event: StagedChangesCommitCodeRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact_changes.events.StagedChangesCommitCodeRequested
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse(
        cls, message: Message
    ) -> StagedChangesCommitCodeRequested:
        """
        Parses given d-bus message containing a StagedChangesCommitCodeRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The StagedChangesCommitCodeRequested event.
        :rtype: pythoneda.shared.artifact_changes.events.StagedChangesCommitCodeRequested
        """
        msg, repository_url, branch, repository_folder, event_id, prev_event_ids = message.body
        return StagedChangesCommitCodeRequested(
            msg, repository_url, branch, repository_folder, None, event_id, json.loads(prev_event_ids)
        )
