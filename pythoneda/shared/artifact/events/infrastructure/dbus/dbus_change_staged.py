# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_change_staged.py

This file defines the DbusChangeStaged class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/events-infrastructure

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
from pythoneda.shared.artifact.events import Change, ChangeStaged
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusChangeStaged(BaseObject, ServiceInterface):
    """
    D-Bus interface for ChangeStaged

    Class name: DbusChangeStaged

    Responsibilities:
        - Define the d-bus interface for the ChangeStaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStaged.
        """
        super().__init__("Pythoneda_Artifact_ChangeStaged")

    @signal()
    def ChangeStaged(self, change: "s"):
        """
        Defines the ChangeStaged d-bus signal.
        :param change: The change.
        :type change: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: ChangeStaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.ChangeStaged
        :return: The event information.
        :rtype: List[str]
        """
        return [event.change.to_json(), event.id, json.dumps(event.previous_event_ids)]

    @classmethod
    def sign(cls, event: ChangeStaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.ChangeStaged
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStaged:
        """
        Parses given d-bus message containing a ChangeStaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStaged event.
        :rtype: pythoneda.shared.artifact.events.ChangeStaged
        """
        change, event_id, prev_event_ids = message.body
        return ChangeStaged(
            Change.from_json(change), None, event_id, json.loads(prev_event_ids)
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
