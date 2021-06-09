def test_docker_is_installed(host):
    # testen, ob das Paket "docker-ce" installiert ist
    docker = host.package("docker-ce")
    assert docker.is_installed

def test_docker_service_is_running(host):
    # testen, ob der Service "docker" läuft und verfügbar ist
    docker = host.service("docker")
    assert docker.is_enabled
    assert docker.is_running

def test_heroapp_container_is_running(host):
    # testen, ob der container mit dem Namen "my-hero-app" läuft
    container = host.docker("my-hero-app")
    assert container.is_running


def test_heroapp_is_available_on_port_80(host):
    # testen, ob auf tcp://0.0.0.0:80 gehorcht wird
    listen = host.socket("tcp://0.0.0.0:80")
    assert listen.is_listening
