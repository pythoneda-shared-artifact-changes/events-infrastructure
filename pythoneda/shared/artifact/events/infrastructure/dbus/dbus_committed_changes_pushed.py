# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_committed_changes_pushed.py

This file defines the DbusCommittedChangesPushed class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/event-infrastructure

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
from pythoneda.shared import BaseObject
from pythoneda.shared.artifact.events import Change, CommittedChangesPushed
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusCommittedChangesPushed(BaseObject, ServiceInterface):
    """
    D-Bus interface for CommittedChangesPushed

    Class name: DbusCommittedChangesPushed

    Responsibilities:
        - Define the d-bus interface for the CommittedChangesPushed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCommittedChangesPushed.
        """
        super().__init__("Pythoneda_Shared_Artifact_Events_CommittedChangesPushed")

    @signal()
    def CommittedChangesPushed(self, change: "s", commit: "s"):
        """
        Defines the CommittedChangesPushed d-bus signal.
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
    def transform(cls, event: CommittedChangesPushed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.CommittedChangesPushed
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
    def sign(cls, event: CommittedChangesPushed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.CommittedChangesPushed
        :return: The signature.
        :rtype: str
        """
        print(f"received event: {event}")
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> CommittedChangesPushed:
        """
        Parses given d-bus message containing a CommittedChangesPushed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CommittedChangesPushed event.
        :rtype: pythoneda.shared.artifact.events.CommittedChangesPushed
        """
        change_json, commit, event_id, prev_event_ids = message.body
        return CommittedChangesPushed(
            Change.from_json(change_json),
            commit,
            None,
            event_id,
            json.loads(prev_event_ids),
        )
