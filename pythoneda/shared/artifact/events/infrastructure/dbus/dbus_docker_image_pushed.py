# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_docker_image_pushed.py

This file defines the DbusDockerImagePushed class.

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
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event, Invariants, PythonedaApplication
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.artifact.events import DockerImagePushed
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List, Tuple, Type


class DbusDockerImagePushed(DbusEvent):
    """
    D-Bus interface for DockerImagePushed.

    Class name: DbusDockerImagePushed

    Responsibilities:
        - Define the d-bus interface for the DockerImagePushed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerImagePushed.
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
        return "Pythoneda_Artifact_DockerImagePushed"

    @signal()
    def DockerImagePushed(
        self,
        imageName: "s",
        imageVersion: "s",
        imageUrl: "s",
        registryUrl: "s",
        metadata: "s",
    ):
        """
        Defines the DockerImagePushed d-bus signal.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        :param imageUrl: The url the image is pushed.
        :type imageUrl: str
        :param registryUrl: The url of the registry.
        :type registryUrl: str
        :param metadata: The image metadata.
        :type metadata: str
        """
        pass

    @property
    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return self.path + "/" + event.image_name.replace("-", "_")

    @classmethod
    def transform(cls, event: DockerImagePushed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.DockerImagePushed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.image_name,
            event.image_version,
            event.image_url,
            event.registry_url,
            json.dumps(event.metadata, ensure_ascii=False),
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: DockerImagePushed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.DockerImagPushed
        :return: The signature.
        :rtype: str
        """
        return "ssssssss"

    @classmethod
    def parse(cls, message: Message, app: PythonedaApplication) -> DockerImagePushed:
        """
        Parses given d-bus message containing a DockerImagePushed event.
        :param message: The message.
        :type message: dbus_next.Message
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.PythonedaApplication
        :return: A tuple with the invariants and the DockerImagePushed event.
        :rtype: Tuple[str, pythoneda.shared.artifact.events.DockerImagePushed]
        """
        (
            image_name,
            image_version,
            image_url,
            registry_url,
            metadata,
            prev_event_ids,
            invariants,
            event_id,
        ) = message.body
        return (
            invariants,
            DockerImagePushed(
                image_name,
                image_version,
                image_url,
                registry_url,
                json.loads(metadata),
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
        return DockerImagePushed


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
