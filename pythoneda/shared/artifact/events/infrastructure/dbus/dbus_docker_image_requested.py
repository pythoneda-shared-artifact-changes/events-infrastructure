# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_docker_image_requested.py

This file defines the DbusDockerImageRequested class.

Copyright (C) 2024-today rydnr's pythoneda-shared-artifact/events-infrastructure

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
from dbus_next import BusType, Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject, Event
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDockerImageRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for DockerImageRequested

    Class name: DbusDockerImageRequested

    Responsibilities:
        - Define the d-bus interface for the DockerImageRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerImageRequested.
        """
        super().__init__("Pythoneda_Artifact_DockerImageRequested")

    @signal()
    def DockerImageRequested(self, imageName: "s", imageVersion: "s"):
        """
        Defines the DockerImageRequested d-bus signal.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/*"

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + event.image_name

    @property
    def bus_type(self) -> str:
        """
        Retrieves the d-bus type.
        :return: Such value.
        :rtype: str
        """
        return BusType.SYSTEM

    @classmethod
    def transform(cls, event: DockerImageRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: org.acmsl.artifact.events.licdata.DockerImageRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.image_name,
            event.image_version,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: DockerImageRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: org.acmsl.artifact.events.licdata.DockerImageRequested
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> DockerImageRequested:
        """
        Parses given d-bus message containing a DockerImageRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DockerImageRequested event.
        :rtype: org.acmsl.artifact.events.licdata.DockerImageRequested
        """
        image_name, image_version, event_id, prev_event_ids = message.body
        return DockerImageRequested(
            image_name, image_version, None, event_id, json.loads(prev_event_ids)
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
