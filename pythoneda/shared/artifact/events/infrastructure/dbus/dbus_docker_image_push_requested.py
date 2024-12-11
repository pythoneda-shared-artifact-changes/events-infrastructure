# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_docker_image_push_requested.py

This file defines the DbusDockerImagePushRequested class.

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
from pythoneda.shared.artifact.events import DockerImagePushRequested
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDockerImagePushRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for DockerImagePushRequested

    Class name: DbusDockerImagePushRequested

    Responsibilities:
        - Define the d-bus interface for the DockerImagePushRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerImagePushRequested.
        """
        super().__init__("Pythoneda_Artifact_DockerImagePushRequested")

    @signal()
    def DockerImagePushRequested(
        self, imageName: "s", imageVersion: "s", registryUrl: "s", metadata: "s"
    ):
        """
        Defines the DockerImagePushRequested d-bus signal.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        :param imageUrl: The url of the image.
        :type imageUrl: str
        :param registryUrl: The url of the registry.
        :type registryUrl: str
        :param metadata: The metadata.
        :type metadata: str
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

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + event.image_name.replace("-", "_")

    @property
    def bus_type(self) -> str:
        """
        Retrieves the d-bus type.
        :return: Such value.
        :rtype: str
        """
        return BusType.SYSTEM

    @classmethod
    def transform(cls, event: DockerImagePushRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.DockerImagePushRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.image_name,
            event.image_version,
            event.image_url,
            event.registry_url,
            json.dumps(event.metadata),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: DockerImagePushRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.DockerImagePushRequested
        :return: The signature.
        :rtype: str
        """
        return "sssssss"

    @classmethod
    def parse(cls, message: Message) -> DockerImagePushRequested:
        """
        Parses given d-bus message containing a DockerImagePushRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DockerImagePushRequested event.
        :rtype: pythoneda.shared.artifact.events.DockerImagePushRequested
        """
        image_name,
        image_version,
        image_url,
        registry_url,
        metadata,
        event_id,
        prev_event_ids = message.body
        return DockerImagePushRequested(
            image_name,
            image_version,
            image_url,
            registry_url,
            json.loads(metadata),
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
