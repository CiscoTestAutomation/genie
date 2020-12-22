.. _template_doc:

Template Documentation
=======================

A parser template documentation is provided along with the parser examples in 
``parser`` directory. The template doc defines the common 
format/structure/guidelines which helps to guide developers to start and 
complete their parser development.

**Template content**:

.. code-block:: text

    #***************************************************************************
    #*                           Parser Template
    #* -------------------------------------------------------------------------
    #* ABOUT THIS TEMPLATE - Please read
    #*
    #* - Any comments with "#*" in front of them (like this entire comment box) 
    #*   are for template clarifications only and should be removed from the 
    #*   final product.
    #*
    #* - Anything enclosed in <> must be replaced by the appropriate text for 
    #*   your application
    #*
    #* Author:
    #*    Ke Liu, Automation Strategy - Core Software Group (CSG)
    #*
    #* Support:
    #*    asg-genie-support@cisco.com
    #*
    #* Description:
    #*   This template file describes how to write a specific parser class by
    #*   inheriting the MetaParser object.
    #*
    #* Read More:
    #*   For the complete and up-to-date user guide on parser template, visit:
    #*   URL= http://wwwin-pyats.cisco.com/documentation/html/parser/index.html
    #*
    #***************************************************************************
    
    #***************************************************************************
    #* DOCSTRINGS
    #*
    #*   All test scripts should use the built-in Python docstrings  
    #*   functionality to define script/class/method headers.
    #*
    #* Format:
    #*   Docstring format should follow:
    #*   URL= http://sphinxcontrib-napoleon.readthedocs.org/en/latest/index.html
    #*
    #* Read More:
    #*   Python Docstrings, PEP 257: 
    #*   URL= http://legacy.python.org/dev/peps/pep-0257/
    #***************************************************************************
    '''template.py
    
    < describe your parser >
    
    Arguments:
        <name> (<type>): <description of your parser argument>
    
    Examples:
        < provide examples on how to use this parser: init and call. >
    
    References:
        < provide references here. >
    
    Notes:
        < provide notes if needed >
    
    '''
    
    #***************************************************************************
    #* OPTIONAL AUTHOR INFORMATION
    #*
    #*   format:
    #*      __author__ = '<first> <last> <email>'
    #*      __copyright__ = 'Copyright 2016, Cisco Systems'
    #*      __credits__ = ['<list>', '<of>', '<names>']
    #*      __maintainer__ = '<team owning/maintaining this script>'
    #*      __email__ = '<email of owners>''
    #*      __date__= '<last modified date>'
    #*      __version__ = <decimal version string>
    #*
    #***************************************************************************
    
    # optional author information
    __author__ = 'Ke Liu <kel2@cisco.com>'
    __copyright__ = 'Copyright 2016, Cisco Systems'
    __credits__ = ["Sedy Yadollahi", 
                   "Siming Yuan", 
                   "Jean-Benoit Aubin"]
    __maintainer__ = 'ASG/ATS team'
    __email__ = 'asg-genie-support@cisco.com'
    __date__= 'May 01, 2016'
    __version__ = 1.0
    
    
    #***************************************************************************
    #* IMPORTS
    #*
    #*   import all modules that are needed in your test script here. Use some 
    #*   form of sorting to make it easy to read. 
    #*
    #* Convention:
    #*   - one module per import for clarity
    #*   - sort imports either alphabetically or per length to give ease of 
    #*     reading, also try to differentiate by functionality/distributor
    #*
    #* Example:
    #*   import os
    #*   import sys
    #*   import xmltodict
    #*   from genie.metaparser import MetaParser
    #*
    #* Read More:
    #*   Python Import System
    #*   URL= https://docs.python.org/3/reference/import.html
    #***************************************************************************
    
    #
    # imports statements
    #
    from genie.metaparser.util.schemaengine import Any
    from genie.metaparser import MetaParser
    
    #***************************************************************************
    #* ShowParser: parser class
    #*
    #* Each module contains at least one parser class which provides the 
    # implementation details of all supported parsing mechanisms (cli(), xml(), 
    #* yang()). Each parser class must inherit from `MetaParser`.
    #*
    #* Class name should be the first 2 words of the 
    #* corresponding cli command or equivalent. For example: class 'ShowVersion' 
    #* to represent 'show version'.
    #*
    #* If the first 2 words contain strong ambiguity (e.g.: show ip),
    #* extend the next word (e.g.: show ip ospf) to clarify the parser purpose.
    #*
    #* For variable phrases within the parser name (e.g.: show interface Eth3/4),
    #* use _WORD_ to present the phrase (e.g.: ShowInterface_WORD_).
    #*
    
    class ShowParser(MetaParser):
    
        '''class ShowParser
    
        parser class - implement detailed parsing mechanisms for cli, xml, and 
        yang output.
    
        Arguments:
            <name> (<type>): <description of your parser argument>
        
        Examples:
            < provide examples on how to initialize this parser. >
        '''
    
        #*************************
        #* class constructor (optional) __init__():
        #* 
        #* In case of redefining __init__ in parser class to overwrite the super
        #* class MetaParser __init__() to support extra attributes, here is an 
        #* example:
        #*     def __init__(self, name, **kwargs):
        #*         super().__init__(name=name, **kwargs)
        
        # <define your own __init__ here, or skip it by using superclass definition>
    
        #*************************
        #* schema - class variable
        #*
        #* schema defines the common data structure among all types of device  
        #* output (cli, xml, yang) the current parser supports. The typical 
        #* scenario is: the first user who defines the first parsing mechanism  
        #* (e.g.: cli ()) in parser class will also define the schema for the 
        #* output structure. At the end of the parsing process, parser engine 
        #* (MetaParser) will do schema checking to make sure the parser always  
        #* returns the output (nested dict) that has the same data structure 
        #* across all supported parsing mechanisms (cli(), yang(), xml()).
        #* 
        #* Example of schema (show version) - nested dict
        #*    schema = {'cmp': {
        #*                    'module': {
        #*                             Any(): {
        #*                                     'bios_compile_time': str,
        #*                                     'bios_version': str,
        #*                                     'image_compile_time': str,
        #*                                     'image_version': str,
        #*                                     'status': str},}},
        #*              'hardware': {
        #*                    'bootflash': str,
        #*                    'chassis': str,
        #*                    'cpu': str,
        #*                    'device_name': str,
        #*                    'memory': str,
        #*                    'model': str,
        #*                    'processor_board_id': str,
        #*                    'slots': str,
        #*                    Any(): Any(),},}
        #*
        #* Here Any() in schema acting like a wildcard character, usually used 
        #* to presenting the variable keys within the dictionary.
        #* For more info on how to use scheme: please read schemaengine API doc.
        #*
    
        # schema = <dict>
    
        #******************************
        #* parsing mechanism: cli
        #* Function cli() defines the cli type output parsing mechanism which
        #* typically contains 3 steps: executing, transforming, returning
        #*
        #* Step1 - executing
        #* User has choices of calling the existing cli parsers from known 
        #* libraries, or implementing new parsing mechanism here 
        #* (eg.: regular expression).
        #*
        #* Example 1 - user implementing parsing mechanism
        #*    parsed_output = {}
        #*    output = self.device.execute("show version | inc 'cisco '")
        #*    m = re.match(r"cisco ([a-zA-Z0-9 ]+)", output.strip(' \t\n\r'))
        #*    if m:
        #*        parsed_output['model'] = m.group(0).strip()
        #* 
        #* Step2 - transforming
        #* This step might be optional for the first parser mechanism writer.
        #* The purpose of this step is to enforce the final output structure 
        #* from all different parsing mechanisms (cli(), xml(), yang()) to be 
        #* same. User can greatly leverage all the functionalities provided in 
        #* metaparser.util class.
        #*
        #* Useful tools to do the transformation:
        #* dict.update()  --> adding missing key-value pairs
        #* metaparser.util.keynames_convert()  --> nested key names converting
        #*
        #* Step3: - returning
        #* return the final result - the structure of the result has to be 
        #* (nested)dictionary
    
        def cli(self, **kwargs):
            # executing parser
            # <step1 executing: get parsing resullt by calling existing backend 
            #        parser function or write user own parsing code here>
            
            # converting the result to compliance with schema
            # <step2: transform the datastructure to be compliance with the 
            #         schema defined on top of the class>
            
            # <step3: return the final parsing result>
            return
    
        #******************************
        #* parsing mechanism: xml
        #* Function xml() defines the xml type output parsing mechanism which
        #* typically contains 3 steps: executing, transforming, returning
        #*
        #* User has choices of calling the existing xml parsers from known 
        #* libraries, or implementing new parsing mechanism here.
        #*
        #* Example - Building xml parser using "xml.etree"
        import xml.etree.ElementTree as ET
        def xml(self, vrf='all'):

            cmd = 'show bgp vrf {} all summary'.format(vrf)

            out = self.device.execute(cmd + ' | xml')

            etree_dict = {}

            # Remove junk characters returned by the device
            out = out.replace("]]>]]>", "")
            root = ET.fromstring(out)

            # top table root
            show_root = Common.retrieve_xml_child(root=root, key='show')
            # get xml namespace
            # {http://www.cisco.com/nxos:7.0.3.I7.1.:bgp}
            try:
                m = re.compile(r'(?P<name>\{[\S]+\})').match(show_root.tag)
                namespace = m.groupdict()['name']
            except Exception:
                return etree_dict

            # compare cli command
            Common.compose_compare_command(root=root, namespace=namespace,
                                           expect_command=cmd)

            # find Vrf root
            root = Common.retrieve_xml_child(root=root, key='TABLE_vrf')

            if not root:
                return etree_dict

            # -----   loop vrf  -----
            for vrf_tree in root.findall('{}ROW_vrf'.format(namespace)):
                # vrf
                try:
                    vrf = vrf_tree.find('{}vrf-name-out'.format(namespace)).text
                except Exception:
                    break

                # <vrf-router-id>19.0.0.6</vrf-router-id>
                try:
                    route_identifier = vrf_tree.find('{}vrf-router-id'.format(namespace)).text
                except Exception:
                    route_identifier = None

                # <vrf-local-as>333</vrf-local-as>
                try:
                    local_as = vrf_tree.find('{}vrf-local-as'.format(namespace)).text
                except Exception:
                    local_as = None

                # Address family table
                af_tree = vrf_tree.find('{}TABLE_af'.format(namespace))
                if not af_tree:
                    continue
                for af_root in af_tree.findall('{}ROW_af'.format(namespace)):
                    # Address family table
                    saf_tree = af_root.find('{}TABLE_saf'.format(namespace))
                    if not saf_tree:
                        continue
                    # -----   loop address_family  -----
                    for saf_root in saf_tree.findall('{}ROW_saf'.format(namespace)):
                        # neighbor
                        try:
                            af = saf_root.find('{}af-name'.format(namespace)).text
                            af = af.lower()
                            # initial af dictionary
                            af_dict = {}
                            if route_identifier:
                                af_dict['route_identifier'] = route_identifier
                            if local_as:
                                af_dict['local_as'] = int(local_as)
                        except Exception:
                            continue

                        # <tableversion>7</tableversion>
                        try:
                            af_dict['bgp_table_version'] = int(
                                saf_root.find('{}tableversion'.format(namespace)).text)
                        except Exception:
                            # for valide entry, table version should be there
                            continue

                        # <configuredpeers>3</configuredpeers>
                        af_dict['config_peers'] = \
                            int(saf_root.find('{}configuredpeers'.format(namespace)).text)
                            
                        # <capablepeers>2</capablepeers>
                        af_dict['capable_peers'] = \
                            int(saf_root.find('{}capablepeers'.format(namespace)).text)

                        # <totalnetworks>5</totalnetworks>
                        try:
                            total_prefix_entries = \
                                int(saf_root.find('{}totalnetworks'.format(namespace)).text)
                            if 'prefixes' not in af_dict:
                                af_dict['prefixes'] = {}
                            af_dict['prefixes']['total_entries'] = total_prefix_entries
                        except Exception:
                            pass
                            
                        # <totalpaths>10</totalpaths>
                        try:
                            total_path_entries = \
                                int(saf_root.find('{}totalpaths'.format(namespace)).text)
                            if 'path' not in af_dict:
                                af_dict['path'] = {}
                            af_dict['path']['total_entries'] = total_path_entries
                        except Exception:
                            pass
                            
                        # <memoryused>1820</memoryused>
                        try:
                            memory_usage = \
                                int(saf_root.find('{}memoryused'.format(namespace)).text)
                            af_dict['path']['memory_usage'] = memory_usage
                            af_dict['prefixes']['memory_usage'] = memory_usage
                        except Exception:
                            pass

                        try:
                            # <numberattrs>1</numberattrs>
                            entries_1 = \
                                saf_root.find('{}numberattrs'.format(namespace)).text
                                
                            # <bytesattrs>160</bytesattrs>
                            entries_2 = \
                                saf_root.find('{}bytesattrs'.format(namespace)).text

                            af_dict['attribute_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                        except Exception:
                            pass
                            
                        try:
                            # <numberpaths>1</numberpaths>
                            entries_1 = \
                                saf_root.find('{}numberpaths'.format(namespace)).text

                            # <bytespaths>34</bytespaths>
                            entries_2 = \
                                saf_root.find('{}bytespaths'.format(namespace)).text

                            af_dict['as_path_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                        except Exception:
                            pass
                            
                        try:
                            # <numbercommunities>0</numbercommunities>
                            entries_1 = \
                                saf_root.find('{}numbercommunities'.format(namespace)).text

                            # <bytescommunities>0</bytescommunities>
                            entries_2 = \
                                saf_root.find('{}bytescommunities'.format(namespace)).text

                            af_dict['community_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                        except Exception:
                            pass
                            
                        try:
                            # <numberclusterlist>0</numberclusterlist>
                            entries_1 = \
                                saf_root.find('{}numberclusterlist'.format(namespace)).text

                            # <bytesclusterlist>0</bytesclusterlist>
                            entries_2 = \
                                saf_root.find('{}bytesclusterlist'.format(namespace)).text

                            af_dict['clusterlist_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                        except Exception:
                            pass

                        # <dampening>Enabled</dampening>
                        dampening = saf_root.find('{}dampening'.format(namespace)).text.lower()
                        if 'enabled' in dampening or 'true' in dampening:
                            af_dict['dampening'] = True

                        # <historypaths>0</historypaths>
                        try:
                            af_dict['history_paths'] = int(saf_root.find('{}historypaths'.format(namespace)).text)
                        except Exception:
                            pass

                        # <dampenedpaths>0</dampenedpaths>
                        try:
                            af_dict['dampened_paths'] = int(saf_root.find('{}dampenedpaths'.format(namespace)).text)
                        except Exception:
                            pass

                        # <softreconfigrecvdpaths>10</softreconfigrecvdpaths>
                        try:
                            af_dict['soft_reconfig_recvd_paths'] = int(
                                    saf_root.find('{}softreconfigrecvdpaths'.format(namespace)).text)
                        except Exception:
                            pass
                            
                        # <softreconfigidenticalpaths>10</softreconfigidenticalpaths>
                        try:
                            af_dict['soft_reconfig_identical_paths'] = int(
                                    saf_root.find('{}softreconfigidenticalpaths'.format(namespace)).text)
                        except Exception:
                            pass

                        # <softreconfigcombopaths>0</softreconfigcombopaths>
                        try:
                            af_dict['soft_reconfig_combo_paths'] = int(
                                    saf_root.find('{}softreconfigcombopaths'.format(namespace)).text)
                        except Exception:
                            pass

                        # <softreconfigfilteredrecvd>0</softreconfigfilteredrecvd>
                        try:
                            af_dict['soft_reconfig_filtered_recvd'] = int(
                                    saf_root.find('{}softreconfigfilteredrecvd'.format(namespace)).text)
                        except Exception:
                            pass
                            
                        # <softreconfigbytes>0</softreconfigbytes>
                        try:
                            af_dict['soft_reconfig_bytes'] = int(
                                    saf_root.find('{}softreconfigbytes'.format(namespace)).text)
                        except Exception:
                            pass
                            
                         # Neighbor table
                        nei_tree = saf_root.find('{}TABLE_neighbor'.format(namespace))
                        if not nei_tree:
                            continue

                        # Construct the returned structure
                        # -----   loop neighbors  -----
                        for nei_root in nei_tree.findall('{}ROW_neighbor'.format(namespace)):
                            # neighbor
                            try:
                                nei = nei_root.find('{}neighborid'.format(namespace)).text
                            except Exception:
                                continue

                            if 'vrf' not in etree_dict:
                                etree_dict['vrf'] = {}
                            if vrf not in etree_dict['vrf']:
                                etree_dict['vrf'][vrf] = {}

                            if 'neighbor' not in etree_dict['vrf'][vrf]:
                                etree_dict['vrf'][vrf]['neighbor'] = {}
                            if nei not in etree_dict['vrf'][vrf]['neighbor']:
                                etree_dict['vrf'][vrf]['neighbor'][nei] = {}

                            if 'address_family' not in etree_dict['vrf'][vrf]['neighbor'][nei]:
                                etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'] = {}

                            if af not in etree_dict['vrf'][vrf]['neighbor'][nei]['address_family']:
                                etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af] = {}
                        
                            sub_dict = etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af]

                            #  ---   AF attributes -------
                            update_dict = deepcopy(af_dict)
                            sub_dict.update(update_dict)

                            #  ---   Neighbors attributes -------
                            # <neighborversion>4</neighborversion>
                            sub_dict['neighbor_table_version'] = int(
                                nei_root.find('{}neighborversion'.format(namespace)).text)
                    
            return etree_dict

        #******************************
        #* parsing mechanism: yang
        #* Function yang() defines the yang type output parsing mechanism which
        #* typically contains 3 steps: executing, transforming, returning
        #*
        #* Step1 - executing
        #* User has choices of calling the existing yang parsers from known 
        #* libraries, or implementing new parsing mechanism here.
        #*
        #* Example - yang parsing mechnism implementation
        from parser.yang.bgp_openconfig_yang import BgpOpenconfigYang
        def yang(self):
            # Initialize empty dictionary
            map_dict = {}

            # Execute YANG 'get' operational state RPC and parse the XML
            bgpOC = BgpOpenconfigYang(self.device)
            yang_dict = bgpOC.yang()

            # Map keys from yang_dict to map_dict

            # bgp_pid
            map_dict['bgp_pid'] = yang_dict['bgp_pid']

            # vrf
            for vrf in yang_dict['vrf']:
                if 'vrf' not in map_dict:
                    map_dict['vrf'] = {}
                if vrf not in map_dict['vrf']:
                    map_dict['vrf'][vrf] = {}
                for vrf_attr_key in yang_dict['vrf'][vrf]:
                    # Set router_id
                    if vrf_attr_key == 'router_id':
                        map_dict['vrf'][vrf][vrf_attr_key] = yang_dict['vrf'][vrf][vrf_attr_key]
                    # Set address_family
                    if vrf_attr_key == 'address_family':
                        map_dict['vrf'][vrf][vrf_attr_key] = yang_dict['vrf'][vrf][vrf_attr_key]
                    if vrf_attr_key == 'neighbor':
                        for nbr in yang_dict['vrf'][vrf]['neighbor']:
                            for key in yang_dict['vrf'][vrf]['neighbor'][nbr]:
                                # Set cluster_id
                                if key == 'route_reflector_cluster_id':
                                    cluster_id = '0.0.0' + str(yang_dict['vrf'][vrf]['neighbor'][nbr]['route_reflector_cluster_id'])
                                    map_dict['vrf'][vrf]['cluster_id'] = cluster_id

            # Return to caller
            return map_dict
