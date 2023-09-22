"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_change_staging_code_execution_requested.py

This file defines the DbusChangeStagingCodeExecutionRequested class.

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
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequest
from pythoneda.shared.artifact_changes.events import ChangeStagingCodeExecutionRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusChangeStagingCodeExecutionRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for ChangeStagingCodeExecutionRequested

    Class name: DbusChangeStagingCodeExecutionRequested

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeExecutionRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeExecutionRequested.
        """
        super().__init__(
            "Pythoneda_Shared_artifact_changes_Events_ChangeStagingCodeExecutionRequested"
        )

    @signal()
    def ChangeStagingCodeExecutionRequested(self, codeRequest: "s"):
        """
        Defines the ChangeStagingExecutionRequested d-bus signal.
        :param codeRequest: The code request.
        :type codeRequest: str
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
    def transform(self, event: ChangeStagingCodeExecutionRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact_changes.events.ChangeStagingCodeExecutionRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.code_request.to_json(),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeExecutionRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact_changes.events.ChangeStagingCodeExecutionRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeExecutionRequested:
        """
        Parses given d-bus message containing a ChangeStagingCodeExecutionRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingExecutionRequested event.
        :rtype: pythoneda.shared.artifact_changes.events.ChangeStagingCodeExecutionRequested
        """
        code_request_json, event_id, prev_event_ids = message.body
        return ChangeStagingCodeExecutionRequested(
            JupyterlabCodeRequest.from_json(code_request_json),
            None,
            event_id,
            json.loads(prev_event_ids),
        )
