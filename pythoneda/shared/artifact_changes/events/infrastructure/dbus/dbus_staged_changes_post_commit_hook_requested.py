"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_staged_changes_post_commit_hook_requested.py

This file defines the DbusStagedChangesPostCommitHookRequested class.

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
from pythoneda.shared.artifact_changes.change import Change
from pythoneda.shared.artifact_changes.events.staged_changes_post_commit_hook_requested import StagedChangesPostCommitHookRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusStagedChangesPostCommitHookRequested(ServiceInterface):
    """
    D-Bus interface for StagedChangesPostCommitHookRequested

    Class name: DbusStagedChangesPostCommitHookRequested

    Responsibilities:
        - Define the d-bus interface for the StagedChangesPostCommitHookRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusStagedChangesPostCommitHookRequested.
        """
        super().__init__("pythonedaartifactchanges_StagedChangesPostCommitHookRequested")

    @signal()
    def StagedChangesPostCommitHookRequested(self, change: "s"):
        """
        Defines the StagedChangesPostCommitHookRequested d-bus signal.
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
    def transform_StagedChangesPostCommitHookRequested(
        self, event: StagedChangesPostCommitHookRequested
    ) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifacteventchanges.staged_changes_post_commit_hook_requested.StagedChangesPostCommitHookRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.event_class,
            event.event_module,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def signature_for_StagedChangesPostCommitHookRequested(
        cls, event: StagedChangesPostCommitHookRequested
    ) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventchanges.staged_changes_post_commit_hook_requested.StagedChangesPostCommitHookRequested
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse_pythonedaartifactchanges_StagedChangesPostCommitHookRequested(
        cls, message: Message
    ) -> StagedChangesPostCommitHookRequested:
        """
        Parses given d-bus message containing a StagedChangesPostCommitHookRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The StagedChangesPostCommitHookRequested event.
        :rtype: pythonedaartifacteventchanges.staged_changes_post_commit_hook_requested.StagedChangesPostCommitHookRequested
        """
        (
            event_class,
            event_module,
            event_id,
            prev_event_ids,
        ) = message.body
        return StagedChangesPostCommitHookRequested(
            event_class,
            event_module,
            None,
            event_id,
            json.loads(prev_event_ids),
        )
