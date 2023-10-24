"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_artifact_commit_pushed.py

This file defines the DbusArtifactCommitPushed class.

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
from pythoneda import BaseObject
from pythoneda.shared.artifact_changes.events import ArtifactCommitPushed
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusArtifactCommitPushed(BaseObject, ServiceInterface):
    """
    D-Bus interface for ArtifactCommitPushed

    Class name: DbusArtifactCommitPushed

    Responsibilities:
        - Define the d-bus interface for the ArtifactCommitPushed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusArtifactCommitPushed.
        """
        super().__init__(
            "Pythoneda_Shared_artifact_changes_Events_ArtifactCommitPushed"
        )

    @signal()
    def ArtifactCommitPushed(self, change: "s", commit: "s"):
        """
        Defines the ArtifactCommitPushed d-bus signal.
        :param change: The change.
        :type change: str
        :param commit: The commit.
        :type commit: str
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
    def transform(self, event: ArtifactCommitPushed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact_changes.events.ArtifactCommitPushed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.change.to_json(),
            event.commit,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: ArtifactCommitPushed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact_changes.events.ArtifactCommitPushed
        :return: The signature.
        :rtype: str
        """
        print(f"received event: {event}")
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> ArtifactCommitPushed:
        """
        Parses given d-bus message containing a ArtifactCommitPushed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ArtifactCommitPushed event.
        :rtype: pythoneda.shared.artifact_changes.events.ArtifactCommitPushed
        """
        change_json, commit, event_id, prev_event_ids = message.body
        return ArtifactCommitPushed(
            Change.from_json(change_json),
            commit,
            None,
            event_id,
            json.loads(prev_event_ids),
        )
