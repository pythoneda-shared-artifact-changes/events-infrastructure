# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_committed_changes_tagged.py

This file defines the DbusCommittedChangesTagged class.

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
from dbus_next.service import signal
import json
from pythoneda.shared import Event, Invariants, PythonedaApplication
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.artifact.events import CommittedChangesTagged
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List, Tuple, Type


class DbusCommittedChangesTagged(DbusEvent):
    """
    D-Bus interface for CommittedChangesTagged

    Class name: DbusCommittedChangesTagged

    Responsibilities:
        - Define the d-bus interface for the CommittedChangesTagged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCommittedChangesTagged.
        """
        super().__init__(DBUS_PATH)

    @classmethod
    @property
    def name(cls) -> str:
        """
        Retrieves the d-bus interface name.
        :return: Such value.
        :rtype: str
        """
        return "Pythoneda_Artifact_CommittedChangesTagged"

    @signal()
    def CommittedChangesTagged(self, commit: "s"):
        """
        Defines the CommittedChangesTagged d-bus signal.
        :param commit: The commit.
        :type commit: str
        """
        pass

    @classmethod
    def transform(cls, event: CommittedChangesTagged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.CommittedChangesTagged
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.tag,
            event.commit,
            event.repository_url,
            event.branch,
            event.repository_folder,
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CommittedChangesTagged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.CommittedChangesTagged
        :return: The signature.
        :rtype: str
        """
        return "ssssssss"

    @classmethod
    def parse(
        cls, message: Message, app: PythonedaApplication
    ) -> Tuple[str, CommittedChangesTagged]:
        """
        Parses given d-bus message containing a CommittedChangesTagged event.
        :param message: The message.
        :type message: dbus_next.Message
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.PythonedaApplication
        :return: A tuple with the invariants and the CommittedChangesTagged event.
        :rtype: Tuple[str, pythoneda.shared.artifact.events.CommittedChangesTagged]
        """
        (
            tag,
            commit,
            repository_url,
            branch,
            folder,
            prev_event_ids,
            invariants,
            event_id,
        ) = message.body
        return (
            invariants,
            CommittedChangesTagged(
                tag,
                commit,
                repository_url,
                branch,
                folder,
                json.loads(prev_event_ids),
                event_id,
            ),
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return CommittedChangesTagged


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
