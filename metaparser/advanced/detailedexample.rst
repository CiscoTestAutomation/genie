Examples
========
.. sidebar:: Helpful Reading

    - :ref:`template_doc`

This section provides an example on how to create a parser class based on 
``metaparser``. A working example ``show_version`` can be found under 
parser directory: ``parser/nxos/show_version.py`` for future 
reference.

What parser to write?
---------------------

Find the equivalent cli which matches the parsing purpose.
Let's give an example: write a nxos xml parser for 'show ipv4 ospf neighbor'.

Check the parser existence
--------------------------

Before starting, it is always recommended to check whether the desired parser 
already exists under ``parser`` directory, or use the GROC tool to 
search. 

**Requirement to name a parser module (parser file)**:
Module name (file name) should be the first two words of the corresponding cli 
command or equivalent. If the first two words contain strong ambiguity 
(e.g.: show ip), extend the next word to clarify the parser purpose.

Therefore, looking for file "show_ipv4_ospf.py" under directory 
``parser/nxos``.

If the parser module does not exist, developer has to create a new 
parser module which contains the desired parser - see `Create a Parser Module`_ 
for detail. 

However, if the parser module looks promising based on the file name, open the 
file and check if it contains the parser class implementation. 

**Requirement to name a parser class**:
We strongly recommend to name the class using the full cli command or 
equivalent to represent the actual parser. For variable phrases within the 
parser class name (e.g.: show interface Eth3/4), use _WORD_ to present the 
phrase (e.g.: ShowInterface_WORD\_).

Therefore, looking for class `ShowIpv4OspfNeighbor` within module 
`show_ipv4_ospf.py`.

If no class is present, developer has to create the parser class - see
`Create a Parser Class`_ for detail.

In case of the parser class has been defined, look into class to further 
check if the desired parsing mechanism - xml() has also been implemented.

If `xml()` function has been defined, and the output structure fulfills the 
developer's expectation - Great! If the parsing output structure does not 
satisfy developer's needs, object-orientation inheritance concept will be 
applied here. However, if the parsing mechanism xm() has not been defined, 
developer has to write the parsing method - see `Implement Parsing Mechanisms`_ 
for detail.

.. _Create a Parser Module:

Create a parser module
----------------------
Parser file contains at least one parser class which includes actual parsing 
mechanisms (cli, xml, yang) implementation. 
All relevant parser classes (name with same starting words) should be 
colocated in the same file. For instance, parser class ShowXxx, ShowXxxYyy, 
and ShowXxxYyyZzz should be implemented in file: show_xxx.py.

Example: create a new file named show_ipv4_ospf.py under ``nxos`` directory

.. _Create a Parser Class:

Create a parser class
---------------------

Example: create parser class named ``ShowIpv4OspfNeighbor`` in parser file 
``show_ipv4_ospf.py``.

Define the parser output schema for this class. The purpose is to make sure the 
parser always returns the output (nested dict) that has the same data structure 
across all supported parsing mechanisms (cli(), yang(), xml()).


.. code-block:: python

    # module show_ipv4_ospf.py
    # ------------------------
    
    # import packages need to use in this module
    from genie.metaparser import MetaParser
    from genie.metaparser.util.schemaengine import Any
    
    # define parser class
    class ShowIpv4OspfNeighbor(MetaParser):

        # define scheme here, Any() in schema acting like a wildcard character, 
        # usually used to presenting the variable keys within the dictionary.
        # For more info on how to define a schema: please read schemaengine API 
        # doc.

        schema = {'intf': {
                        Any(): {
                            'neighbor': str,
                            'interface_address': str,
                            'process_id': str,
                            'vrf': str,
                            'area': str,
                            'state': str,
                            'dr': str,
                            'bdr': str,},},
                  'intf_list': str,}


.. _Implement Parsing Mechanisms:

Implement parsing mechanisms
----------------------------

Current parser infra supports 'cli', 'xml', and 'yang' as its parsing 
mechanisms. Each parsing mechanism will be implemented as a Python method 
within the parser class.

Example: implement class method xml().

Function xml() defines the xml type output parsing mechanism which
typically contains 3 steps: executing, transforming, and returning.
    * Step1 - executing
    Developer has choices of calling the existing xml parsers from known
    libraries, or implementing new parsing mechanism here.

    * Step2 - transforming
    This step might be optional for the first parser mechanism writer.
    The purpose of this step is to enforce the final output structure from
    all different parsing mechanisms (cli(), xml(), yang()) to be same.
    Developer can greatly leverage all the functionalities provided in 
    ``metaparser.util`` class.

    Useful tools to do the transformation:
    dict.update()  --> adding missing key-value pairs
    metaparser.util.keynames_convert()  --> nested key names converting
    
    * Step3: - returning
    Returns the final result - the structure of the result has to be 
    (nested)dictionary.
    
    For detail example, please read :ref:`template_doc`, and reference the 
    example: ``parser/nxos/show_platform.py``.

.. code-block:: python

    def xml(self):
        out = self.device.execute('show ipv4 ospf neighbor | xml')

        etree_dict = {}
        # Remove junk characters returned by the device
        out = out.replace("]]>]]>", "")
        output = ET.fromstring(out)

        for item in output:
            for data in item:
                for show in data:
                    for ospf in show:
                        for __XML__OPT_Cmd_show_ip_ospf_session_cmd_vrf in ospf:
                            for process in __XML__OPT_Cmd_show_ip_ospf_session_cmd_vrf:
                                for __XML__OPT_Cmd_show_ospf_process_cmd_vrf in process:
                                    for __XML__OPT_Cmd_show_ospf_process_cmd___readonly__ in __XML__OPT_Cmd_show_ospf_process_cmd_vrf:
                                        for key in __XML__OPT_Cmd_show_ospf_process_cmd___readonly__:
                                            # Get key text
                                            text = key.tag[key.tag.find('}')+1:]
                                            # ospf_pid
                                            if text == 'processid':
                                                etree_dict['ospf_pid'] = int(key.text)
                                            # ospf_protocol_started_reason
                                            if text == 'protocolstartedreason':
                                                etree_dict['ospf_protocol_started_reason'] = key.text
                                            # ospf_tag
                                            if text == 'protocoltag':
                                                etree_dict['ospf_tag'] = key.text
                                            # ospf_protocol_state
                                            if text == 'protocolstate':
                                                etree_dict['ospf_protocol_state'] = str(key.text).lower()
                                            # ospf_isolate_mode
                                            if text == 'isolatemode':
                                                etree_dict['ospf_isolate_mode'] = key.text
                                            # ospf_mmode
                                            if text == 'mmode':
                                                etree_dict['ospf_mmode'] = key.text
                                            # ospf_memory_state
                                            if text == 'memorystate':
                                                etree_dict['ospf_memory_state'] = str(key.text).lower()
                                            # ospf_performance_mode
                                            if text == 'forwardingstatesaved':
                                                if key.text == 'false':
                                                    etree_dict['ospf_performance_mode'] = 'No'
                                                else:
                                                    etree_dict['ospf_performance_mode'] = 'Yes'
                                            # ospf_asformat
                                            if text == 'asformat':
                                                etree_dict['ospf_asformat'] = key.text
                                            if text == 'srgbmin':
                                                srgbin = key.text
                                            if text == 'srgbmax':
                                                srgmax = key.text
                                                try:
                                                    etree_dict['segment_routing_global_block'] = srgbin + '-' + srgmax
                                                except Exception:
                                                    pass
                                            # num_attr_entries
                                            if text == 'attributeentries':
                                                etree_dict['num_attr_entries'] = int(key.text)
                                            # hwm_attr_entries
                                            if text == 'hwmattributeentries':
                                                etree_dict['hwm_attr_entries'] = int(key.text)
                                            # bytes_used
                                            if text == 'bytesused':
                                                etree_dict['bytes_used'] = int(key.text)
                                            # entries_pending_delete
                                            if text == 'entriespendingdelete':
                                                etree_dict['entries_pending_delete'] = int(key.text)
                                            # hwm_entries_pending_delete
                                            if text == 'hwmentriespendingdelete':
                                                etree_dict['hwm_entries_pending_delete'] = int(key.text)
                                            # ospf_paths_per_hwm_attr
                                            if text == 'pathsperattribute':
                                                etree_dict['ospf_paths_per_hwm_attr'] = int(key.text)
                                            # ospf_as_path_entries
                                            if text == 'aspathentries':
                                                etree_dict['ospf_as_path_entries'] = int(key.text)
                                            # bytes_used_as_path_entries
                                            if text == 'aspathbytes':
                                                etree_dict['bytes_used_as_path_entries'] = int(key.text)
                                            
                                            if text == 'TABLE_vrf':
                                                for table_vrf in key:
                                                    for row_vrf in table_vrf:
                                                        vrf_tag = row_vrf.tag[row_vrf.tag.find('}')+1:]

                                                        # vrf
                                                        #   vrf_name
                                                        if vrf_tag == 'vrf-name-out':
                                                            vrf_name = row_vrf.text
                                                            if 'vrf' not in etree_dict:
                                                                etree_dict['vrf'] = {}
                                                            if vrf_name not in etree_dict['vrf']:
                                                                etree_dict['vrf'][vrf_name] = {}
                                                                vrf_dict = etree_dict['vrf'][vrf_name]
                                                        # vrf_id
                                                        if vrf_tag == 'vrf-id':
                                                            vrf_dict['vrf_id'] = row_vrf.text
                                                        # vrf_state
                                                        if vrf_tag == 'vrf-state':
                                                            vrf_dict['vrf_state'] = str(row_vrf.text).lower()
                                                        # router_id
                                                        if vrf_tag == 'vrf-router-id':
                                                            vrf_dict['router_id'] = row_vrf.text
                                                        # conf_router_id
                                                        if vrf_tag == 'vrf-cfgd-id':
                                                            vrf_dict['conf_router_id'] = row_vrf.text
                                                        # confed_id
                                                        if vrf_tag == 'vrf-confed-id':
                                                            vrf_dict['confed_id'] = int(row_vrf.text)
                                                        # cluster_id
                                                        if vrf_tag == 'vrf-cluster-id':
                                                           vrf_dict['cluster_id'] = row_vrf.text
                                                        # num_conf_peers
                                                        if vrf_tag == 'vrf-peers':
                                                            vrf_dict['num_conf_peers'] = int(row_vrf.text)
                                                        # num_pending_conf_peers
                                                        if vrf_tag == 'vrf-pending-peers':
                                                            vrf_dict['num_pending_conf_peers'] = int(row_vrf.text)
                                                        # num_established_peers
                                                        if vrf_tag == 'vrf-est-peers':
                                                            vrf_dict['num_established_peers'] = int(row_vrf.text)
                                                            vrf_dict['vrf_rd'] = 'not configured'
                                                        # vrf_rd
                                                        if vrf_tag == 'vrf-rd':
                                                            vrf_dict['vrf_rd'] = row_vrf.text

                                                        if vrf_tag == 'TABLE_af':
                                                            for table_af in row_vrf:
                                                                for row_af in table_af:
                                                                    af_tag = row_af.tag[row_af.tag.find('}')+1:]

                                                                    # address_family
                                                                    #   address_family_name
                                                                    if af_tag == 'af-name':
                                                                        address_family_name = str(row_af.text).lower()
                                                                        if 'address_family' not in etree_dict['vrf'][vrf_name]:
                                                                            etree_dict['vrf'][vrf_name]['address_family'] = {}
                                                                        if address_family_name not in etree_dict['vrf'][vrf_name]['address_family']:
                                                                            etree_dict['vrf'][vrf_name]['address_family'][address_family_name] = {}
                                                                            af_dict = etree_dict['vrf'][vrf_name]['address_family'][address_family_name]
                                                                        # Initialize empty lists
                                                                        export_rt_list = ''
                                                                        import_rt_list = ''
                                                                    # table_id
                                                                    if af_tag == 'af-table-id':
                                                                        table_id = str(row_af.text)
                                                                        if '0x' in table_id:
                                                                            af_dict['table_id'] = table_id
                                                                        else:
                                                                            af_dict['table_id'] = '0x' + table_id
                                                                    # table_state
                                                                    if af_tag == 'af-state':
                                                                        af_dict['table_state'] = str(row_af.text).lower()
                                                                    # peers
                                                                    if af_tag == 'af-num-peers':
                                                                        peers = int(row_af.text)
                                                                        if 'peers' not in af_dict:
                                                                            af_dict['peers'] = {}
                                                                        if peers not in af_dict['peers']:
                                                                            af_dict['peers'][peers] = {}
                                                                    # active_peers
                                                                    if af_tag == 'af-num-active-peers':
                                                                        af_dict['peers'][peers]['active_peers'] = int(row_af.text)
                                                                    # routes
                                                                    if af_tag == 'af-peer-routes':
                                                                        af_dict['peers'][peers]['routes'] = int(row_af.text)
                                                                    # paths
                                                                    if af_tag == 'af-peer-paths':
                                                                        af_dict['peers'][peers]['paths'] = int(row_af.text)
                                                                    # networks
                                                                    if af_tag == 'af-peer-networks':
                                                                        af_dict['peers'][peers]['networks'] = int(row_af.text)
                                                                    # aggregates
                                                                    if af_tag == 'af-peer-aggregates':
                                                                        af_dict['peers'][peers]['aggregates'] = int(row_af.text)
                                                                    # route_reflector
                                                                    if af_tag == 'af-rr':
                                                                        if row_af.text == 'true':
                                                                            af_dict['route_reflector'] = True
                                                                    # next_hop_trigger_delay
                                                                    #   critical
                                                                    if af_tag == 'nexthop-trigger-delay-critical':
                                                                        if 'next_hop_trigger_delay' not in af_dict:
                                                                            af_dict['next_hop_trigger_delay'] = {}
                                                                        af_dict['next_hop_trigger_delay']['critical'] = int(row_af.text)
                                                                    # next_hop_trigger_delay
                                                                    #   non_critical
                                                                    if af_tag == 'nexthop-trigger-delay-non-critical':
                                                                        af_dict['next_hop_trigger_delay']['non_critical'] = int(row_af.text)
                                                                    # aggregate_label
                                                                    if af_tag == 'af-aggregate-label':
                                                                        af_dict['aggregate_label'] = row_af.text
                                                                    # label_mode
                                                                    if af_tag == 'af-label-mode':
                                                                        af_dict['label_mode'] = row_af.text
                                                                    # import_default_map
                                                                    if af_tag == 'importdefault_map':
                                                                        af_dict['import_default_map'] = row_af.text
                                                                    # import_default_prefix_limit
                                                                    if af_tag == 'importdefault_prefixlimit':
                                                                        af_dict['import_default_prefix_limit'] = int(row_af.text)
                                                                    # import_default_prefix_count
                                                                    if af_tag == 'importdefault_prefixcount':
                                                                        af_dict['import_default_prefix_count'] = int(row_af.text)
                                                                    # export_default_map
                                                                    if af_tag == 'exportdefault_map':
                                                                        af_dict['export_default_map'] = row_af.text
                                                                    # export_default_prefix_limit
                                                                    if af_tag == 'exportdefault_prefixlimit':
                                                                        af_dict['export_default_prefix_limit'] = int(row_af.text)
                                                                    # export_default_prefix_count
                                                                    if af_tag == 'exportdefault_prefixcount':
                                                                        af_dict['export_default_prefix_count'] = int(row_af.text)

                                                                    # TABLE_redist
                                                                    #   ROW_redist
                                                                    if af_tag == 'TABLE_redist':
                                                                        for table_redist in row_af:
                                                                            for row_redist in table_redist:
                                                                                row_redist_tag = row_redist.tag[row_redist.tag.find('}')+1:]
                                                                                # protocol
                                                                                if row_redist_tag == 'protocol':
                                                                                    protocol = row_redist.text
                                                                                    if 'redistribution' not in af_dict:
                                                                                        af_dict['redistribution'] = {}
                                                                                    if protocol not in af_dict['redistribution']:
                                                                                        af_dict['redistribution'][protocol] = {}
                                                                                # route_map
                                                                                if row_redist_tag == 'route-map':
                                                                                    af_dict['redistribution'][protocol]['route_map'] = row_redist.text

                                                                    # TABLE_evpn_export_rt
                                                                    #   ROW_evpn_export_rt
                                                                    if af_tag == 'TABLE_evpn_export_rt':
                                                                        for table_evpn_export in row_af:
                                                                            for row_export in table_evpn_export:
                                                                                row_export_tag = row_export.tag[row_export.tag.find('}')+1:]
                                                                                # export_rt_list
                                                                                if row_export_tag == 'evpn-export-rt':
                                                                                    export_rt_list = str(export_rt_list + ' ' + row_export.text).strip()
                                                                                    af_dict['export_rt_list'] = export_rt_list
                                                                    # TABLE_evpn_import_rt
                                                                    #   ROW_evpn_import_rt
                                                                    if af_tag == 'TABLE_evpn_import_rt':
                                                                        for table_evpn_import in row_af:
                                                                            for row_import in table_evpn_import:
                                                                                row_import_tag = row_import.tag[row_import.tag.find('}')+1:]
                                                                                # export_rt_list
                                                                                if row_import_tag == 'evpn-import-rt':
                                                                                    import_rt_list = str(import_rt_list + ' ' + row_import.text).strip()
                                                                                    af_dict['import_rt_list'] = import_rt_list

                                                                    # parsed all tags
                                                                    continue
                                                                                    
        return etree_dict

XML Parser Using ETree
^^^^^^^^^^^^^^^^^^^^^^

Please refer to this file for an example :ref:`xmlregex`

XML Parser Using Regular Expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to this file for an example :ref:`xmletree`
      