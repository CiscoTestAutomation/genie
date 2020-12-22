.. _virl:

VIRL
====

.. sidebar:: Quick References

    - :virl_tutorials:`Virl Tutorials <http>`
    - :cisco_virl:`Cisco VIRL - YouTube <http>`


VIRL (Virtual Internet Routing Lab) is Cisco's powerful network simulation
platform, with Cisco OS virtual machines shipped with the software package.

It's your flexible, all-in-one virtual networking lab. No more bulky network
equipment and hours of wiring! Easy-to-build connections to actual networking
equipment or to extend your lab by linking physical and virtual networking
devices.


DevNet user
-----------

1. Get :virl:`virl <http>`. The license needs to be purchased.


2. Install VIRL depending on type of your platform.

    - :windows:`Windows <http>`
    - :mac:`Mac <http>`
    - :vsphere:`vSphere <http>`

3. Download sample virl files as below.

    - :download:`example_testbed.virl <example_testbed.virl>`.
    - :download:`example_testbed_empty.virl <example_testbed_empty.virl>`.

4. Load the virl file on VIRL and launch the topology.

    - Access to UWM and login with your credential. (default: uwmadmin/password)

      http://<VIRL VM IP Address/

      .. figure:: first_login.png

    - Click "My Simulations" from left side menu.

      .. figure:: simulations.png

    - Click "Launch new simulation"

      .. figure:: launch_sim.png

    - Select "Local .virl file" and select the downloaded "example_testbed.virl". And then click 'Launch".

      .. figure:: select_local_virl.png

      The page will be changed and you can find below table after some time. Please make sure below 2 device are active state and take a note following ip address and port number in red box for 2 devices.

      .. figure:: nodes.png


5. Below is a sample testbed yaml file.

    - :download:`testbed.yaml <testbed.yaml>`.



    .. note::

        - Machine where pyATS/Genie are running should have a reachability to the IP address in Step4
        - Replace the '<ip address>', '<port>' with what you took a note in Step4.


Cisco employee
--------------

1. Get :virl:`virl <http>` image from below page.

    PC/Mac : virl.xxxx.pc.ova
    ESXi / vSphere : virl.xxxx.esxi.ova

2. Install VIRL depending on type of your platform.

    - :windows:`Windows <http>`
    - :mac:`Mac <http>`
    - :vsphere:`vSphere <http>`

3. Download sample virl files as below.

    - :download:`example_testbed.virl <example_testbed.virl>`.
    - :download:`example_testbed_empty.virl <example_testbed_empty.virl>`.

4. Load the virl file on VIRL and launch the topology.

    - Access to UWM and login with your credential. (default: uwmadmin/password)
      http://<VIRL VM IP Address/

      .. figure:: first_login.png

    - Click "My Simulations" from left side menu.

      .. figure:: simulations.png

    - Click "Launch new simulation"

      .. figure:: launch_sim.png

    - Select "Local .virl file" and select the downloaded "example_testbed.virl". And then click 'Launch".

      .. figure:: select_local_virl.png

      The page will be changed and you can find below table after some time. Please make sure below 2 device are active state and take a note following ip address and port number in red box for 2 devices.

      .. figure:: nodes.png


5. Below is a sample testbed yaml file.

    - :download:`testbed.yaml <testbed.yaml>`.



    .. note::

        - Machine where pyATS/Genie are running should have a reachability to the IP address in Step4
        - Replace the '<ip address>', '<port>' with what you took a note in Step4.