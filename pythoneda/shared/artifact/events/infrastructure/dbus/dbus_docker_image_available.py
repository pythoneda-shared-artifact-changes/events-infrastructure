# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_docker_image_available.py

This file defines the DbusDockerImageAvailable class.

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
from pythoneda.shared.artifact.events import DockerImageAvailable
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List, Tuple, Type


class DbusDockerImageAvailable(DbusEvent):
    """
    D-Bus interface for DockerImageAvailable

    Class name: DbusDockerImageAvailable

    Responsibilities:
        - Define the d-bus interface for the DockerImageAvailable event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerImageAvailable.
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
        return "Pythoneda_Artifact_DockerImageAvailable"

    @signal()
    def DockerImageAvailable(self, imageName: "s", imageVersion: "s", imageUrl: "s"):
        """
        Defines the DockerImageAvailable d-bus signal.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        :param imageUrl: The url the image is available.
        :type imageUrl: str
        """
        pass

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + self.sanitize_path(event.image_name)

    @classmethod
    def transform(cls, event: DockerImageAvailable) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.DockerImagAvailable
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.image_name,
            event.image_version,
            event.image_url,
            json.dumps(event.metadata, ensure_ascii=False),
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: DockerImageAvailable) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.DockerImagAvailable
        :return: The signature.
        :rtype: str
        """
        return "sssssss"

    @classmethod
    def parse(
        cls, message: Message, app: PythonedaApplication
    ) -> Tuple[str, DockerImageAvailable]:
        """
        Parses given d-bus message containing a DockerImageAvailable event.
        :param message: The message.
        :type message: dbus_next.Message
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.PythonedaApplication
        :return: A tuple with the invariants and the DockerImageAvailable event.
        :rtype: Tuple[str, pythoneda.shared.artifact.events.DockerImageAvailable]
        """
        (
            image_name,
            image_version,
            image_url,
            metadata,
            prev_event_ids,
            invariants,
            event_id,
        ) = message.body
        return (
            invariants,
            DockerImageAvailable(
                image_name,
                image_version,
                image_url,
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
        return DockerImageAvailable


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
