.. _xmlregex:

XML Parser Using Regular Expressions
""""""""""""""""""""""""""""""""""""

.. code-block:: python

    class ShowBgpProcessVrfAllSchema(MetaParser):
        
        '''Schema for show bgp process vrf all'''

        schema = {
            'bgp_pid': int,
            'bgp_protocol_started_reason': str,
            Optional('bgp_performance_mode'): str,
            'bgp_tag': str,
            'bgp_protocol_state': str,
            Optional('bgp_isolate_mode'): str,
            Optional('bgp_mmode'): str,
            'bgp_memory_state': str,
            Optional('bgp_asformat'): str,
            Optional('segment_routing_global_block'): str,
            'num_attr_entries': int,
            'hwm_attr_entries': int,
            'bytes_used': int,
            'entries_pending_delete': int,
            'hwm_entries_pending_delete': int,
            'bgp_paths_per_hwm_attr': int,
            'bgp_as_path_entries': int,
            'bytes_used_as_path_entries': int,
            Optional('vrf'): 
                {Any(): 
                    {'vrf_id': str,
                     'vrf_state': str,
                     Optional('router_id'): str,
                     Optional('conf_router_id'): str,
                     Optional('confed_id'): int,
                     Optional('cluster_id'): str,
                     'num_conf_peers': int,
                     'num_pending_conf_peers': int,
                     'num_established_peers': int,
                     Optional('vrf_rd'): str,
                     Optional('address_family'): 
                        {Any(): 
                            {Optional('table_id'): str,
                             Optional('table_state'): str,
                             'peers': 
                                {Any(): 
                                    {'active_peers': int,
                                     'routes': int,
                                     'paths': int,
                                     'networks': int,
                                     'aggregates': int,
                                    },
                                },
                             Optional('redistribution'): 
                                {Any(): 
                                    {Optional('route_map'): str,
                                    },
                                },
                             Optional('export_rt_list'): str,
                             Optional('import_rt_list'): str,
                             Optional('label_mode'): str,
                             Optional('aggregate_label'): str,
                             Optional('route_reflector'): bool,
                             Optional('next_hop_trigger_delay'):
                                {'critical': int,
                                 'non_critical': int,
                                },
                            Optional('import_default_map'): str,
                            Optional('import_default_prefix_limit'): int,
                            Optional('import_default_prefix_count'): int,
                            Optional('export_default_map'): str,
                            Optional('export_default_prefix_limit'): int,
                            Optional('export_default_prefix_count'): int,
                            },
                        },
                    },
                },
            }

    class ShowBgpProcessVrfAll(ShowBgpProcessVrfAllSchema):

        '''Parser for show bgp process vrf all'''

        def xml(self, parser=None):
            out = self.device.execute('show bgp process vrf all | xml')

            # Init vars
            parsed_dict = {}

            for line in out.splitlines():
                line = line.rstrip()

                # <processid>29663</processid>
                p1 = re.compile(r'^\s*\<processid\>(?P<processid>[0-9]+)'
                                 '\<\/processid\>$')
                m = p1.match(line)
                if m:
                    parsed_dict['bgp_pid'] = int(m.groupdict()['processid'])
                    continue

                # <protocolstartedreason>configuration</protocolstartedreason>
                p2 = re.compile(r'^\s*\<protocolstartedreason\>'
                                 '(?P<protocolstartedreason>[a-zA-Z\s]+)'
                                 '\<\/protocolstartedreason\>$')
                m = p2.match(line)
                if m:
                    parsed_dict['bgp_protocol_started_reason'] = \
                        str(m.groupdict()['protocolstartedreason'])
                    continue

                # <protocoltag>333</protocoltag>
                p3 = re.compile(r'^\s*\<protocoltag\>(?P<protocoltag>[0-9]+)'
                                 '\<\/protocoltag\>$')
                m = p3.match(line)
                if m:
                    parsed_dict['bgp_tag'] = str(m.groupdict()['protocoltag'])
                    continue

                # <protocolstate>Running</protocolstate>
                p4 = re.compile(r'^\s*\<protocolstate\>(?P<protocolstate>[a-zA-Z]+)'
                                 '\<\/protocolstate\>$')
                m = p4.match(line)
                if m:
                    parsed_dict['bgp_protocol_state'] = \
                        str(m.groupdict()['protocolstate'])
                    continue

                # <isolatemode>No</isolatemode>
                p5 = re.compile(r'^\s*\<isolatemode\>(?P<isolatemode>([a-zA-Z])+)'
                                 '\<\/isolatemode\>$')
                m = p5.match(line)
                if m:
                    parsed_dict['bgp_isolate_mode'] = \
                        str(m.groupdict()['isolatemode'])
                    continue

                # <mmode>Initialized</mmode>
                p6 = re.compile(r'^\s*\<mmode\>(?P<mmode>([a-zA-Z])+)\<\/mmode\>$')
                m = p6.match(line)
                if m:
                    parsed_dict['bgp_mmode'] = str(m.groupdict()['mmode'])
                    continue

                # <memorystate>OK</memorystate>
                p7 = re.compile(r'^\s*\<memorystate\>(?P<memorystate>([a-zA-Z])+)'
                                 '\<\/memorystate\>$')
                m = p7.match(line)
                if m:
                    parsed_dict['bgp_memory_state'] = \
                        str(m.groupdict()['memorystate'])
                    continue

                # <forwardingstatesaved>false</forwardingstatesaved>
                p7_1 = re.compile(r'^\s*\<forwardingstatesaved\>'
                                   '(?P<forwardingstatesaved>([a-zA-Z])+)'
                                   '\<\/forwardingstatesaved\>$')
                m = p7_1.match(line)
                if m:
                    state = str(m.groupdict()['forwardingstatesaved'])
                    if state == 'false':
                        parsed_dict['bgp_performance_mode'] = 'No'
                    else:
                        parsed_dict['bgp_performance_mode'] = 'Yes'
                    continue

                # <asformat>asplain</asformat>
                p8 = re.compile(r'^\s*\<asformat\>(?P<asformat>([a-zA-Z])+)'
                                 '\<\/asformat\>$')
                m = p8.match(line)
                if m:
                    parsed_dict['bgp_asformat'] = str(m.groupdict()['asformat'])
                    continue

                # <srgbmin>10000</srgbmin>
                p9_1 = re.compile(r'^\s*\<srgbmin\>(?P<srgbmin>([0-9])+)'
                                   '\<\/srgbmin\>$')
                m = p9_1.match(line)
                if m:
                    srgbmin = str(m.groupdict()['srgbmin'])
                    continue

                # <srgbmax>25000</srgbmax>
                p9_2 = re.compile(r'^\s*\<srgbmax\>(?P<srgbmax>([0-9])+)'
                                   '\<\/srgbmax\>$')
                m = p9_2.match(line)
                if m:
                    srgbmax = str(m.groupdict()['srgbmax'])
                    parsed_dict['segment_routing_global_block'] = \
                        str(srgbmin + '-' + srgbmax)
                    continue

                # <attributeentries>4</attributeentries>
                p10 = re.compile(r'^\s*\<attributeentries\>'
                                  '(?P<attributeentries>([0-9])+)'
                                  '\<\/attributeentries\>$')
                m = p10.match(line)
                if m:
                    parsed_dict['num_attr_entries'] = \
                        int(m.groupdict()['attributeentries'])
                    continue

                # <hwmattributeentries>4</hwmattributeentries>
                p11 = re.compile(r'^\s*\<hwmattributeentries\>'
                                  '(?P<hwmattributeentries>([0-9])+)'
                                  '\<\/hwmattributeentries\>$')
                m = p11.match(line)
                if m:
                    parsed_dict['hwm_attr_entries'] = \
                        int(m.groupdict()['hwmattributeentries'])
                    continue

                # <bytesused>448</bytesused>
                p12 = re.compile(r'^\s*\<bytesused\>'
                                  '(?P<bytesused>([0-9])+)\<\/bytesused\>$')
                m = p12.match(line)
                if m:
                    parsed_dict['bytes_used'] = int(m.groupdict()['bytesused'])
                    continue

                # <entriespendingdelete>0</entriespendingdelete>
                p13 = re.compile(r'^\s*\<entriespendingdelete\>'
                                  '(?P<entriespendingdelete>([0-9])+)'
                                  '\<\/entriespendingdelete\>$')
                m = p13.match(line)
                if m:
                    parsed_dict['entries_pending_delete'] = \
                        int(m.groupdict()['entriespendingdelete'])
                    continue

                # <hwmentriespendingdelete>0</hwmentriespendingdelete>
                p14 = re.compile(r'^\s*\<hwmentriespendingdelete\>'
                                  '(?P<hwmentriespendingdelete>([0-9])+)'
                                  '\<\/hwmentriespendingdelete\>$')
                m = p14.match(line)
                if m:
                    parsed_dict['hwm_entries_pending_delete'] = \
                        int(m.groupdict()['hwmentriespendingdelete'])
                    continue

                # <pathsperattribute>3</pathsperattribute>
                p15 = re.compile(r'^\s*\<pathsperattribute\>'
                                  '(?P<pathsperattribute>([0-9])+)'
                                  '\<\/pathsperattribute\>$')
                m = p15.match(line)
                if m:
                    parsed_dict['bgp_paths_per_hwm_attr'] = \
                        int(m.groupdict()['pathsperattribute'])
                    continue

                # <aspathentries>0</aspathentries>
                p16 = re.compile(r'^\s*\<aspathentries\>(?P<aspathentries>([0-9])+)'
                                  '\<\/aspathentries\>$')
                m = p16.match(line)
                if m:
                    parsed_dict['bgp_as_path_entries'] = \
                        int(m.groupdict()['aspathentries'])
                    continue

                # <aspathbytes>0</aspathbytes>
                p17 = re.compile(r'^\s*\<aspathbytes\>(?P<aspathbytes>([0-9])+)'
                                  '\<\/aspathbytes\>$')
                m = p17.match(line)
                if m:
                    parsed_dict['bytes_used_as_path_entries'] = \
                        int(m.groupdict()['aspathbytes'])
                    continue

                # <vrf-name-out>vpn1</vrf-name-out>
                p18 = re.compile(r'^\s*\<vrf\-name\-out\>'
                                  '(?P<vrf_name>([a-zA-Z0-9])+)'
                                  '\<\/vrf\-name\-out\>$')
                m = p18.match(line)
                if m:
                    if 'vrf' not in parsed_dict:
                        parsed_dict['vrf'] = {}
                    vrf_name = str(m.groupdict()['vrf_name'])
                    if vrf_name not in parsed_dict['vrf']:
                        parsed_dict['vrf'][vrf_name] = {}
                        continue

                # <vrf-id>4</vrf-id>\
                p19 = re.compile(r'^\s*\<vrf\-id\>(?P<vrf_id>([a-zA-Z0-9])+)'
                                  '\<\/vrf\-id\>$')
                m = p19.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['vrf_id'] = \
                        str(m.groupdict()['vrf_id'])
                    continue

                # <vrf-state>UP</vrf-state>
                p20 = re.compile(r'^\s*\<vrf\-state\>(?P<vrf_state>([a-zA-Z])+)'
                                  '\<\/vrf\-state\>$')
                m = p20.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['vrf_state'] = \
                        str(m.groupdict()['vrf_state'])
                    continue

                # <vrf-delete-pending>false</vrf-delete-pending>

                # <vrf-router-id>0.0.0.0</vrf-router-id>
                p21 = re.compile(r'^\s*\<vrf\-router\-id\>'
                                  '(?P<router_id>([0-9\.\:])+)'
                                  '\<\/vrf\-router\-id\>$')
                m = p21.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['router_id'] = \
                        str(m.groupdict()['router_id'])
                    continue

                # <vrf-cfgd-id>0.0.0.0</vrf-cfgd-id>
                p22 = re.compile(r'^\s*\<vrf\-cfgd\-id\>'
                                  '(?P<conf_router_id>([0-9\.\:])+)'
                                  '\<\/vrf\-cfgd\-id\>$')
                m = p22.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['conf_router_id'] = \
                        str(m.groupdict()['conf_router_id'])
                    continue

                # <vrf-confed-id>0</vrf-confed-id>
                p23 = re.compile(r'^\s*\<vrf\-confed\-id\>'
                                  '(?P<confed_id>([0-9])+)\<\/vrf\-confed\-id\>$')
                m = p23.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['confed_id'] = \
                        int(m.groupdict()['confed_id'])
                    continue

                # <vrf-cluster-id>0.0.0.0</vrf-cluster-id>
                p24 = re.compile(r'^\s*\<vrf\-cluster\-id\>'
                                  '(?P<cluster_id>([0-9\.\:])+)'
                                  '\<\/vrf\-cluster\-id\>$')
                m = p24.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['cluster_id'] = \
                        str(m.groupdict()['cluster_id'])
                    continue

                # <vrf-peers>0</vrf-peers>
                p25 = re.compile(r'^\s*\<vrf\-peers\>'
                                  '(?P<num_conf_peers>([0-9])+)\<\/vrf\-peers\>$')
                m = p25.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['num_conf_peers'] = \
                        int(m.groupdict()['num_conf_peers'])
                    continue

                # <vrf-pending-peers>0</vrf-pending-peers>
                p26 = re.compile(r'^\s*\<vrf\-pending\-peers\>'
                                  '(?P<num_pending_conf_peers>([0-9])+)'
                                  '\<\/vrf\-pending\-peers\>$')
                m = p26.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['num_pending_conf_peers'] = \
                        int(m.groupdict()['num_pending_conf_peers'])
                    continue

                # <vrf-est-peers>0</vrf-est-peers>
                p27 = re.compile(r'^\s*\<vrf\-est\-peers\>'
                                  '(?P<num_established_peers>([0-9])+)'
                                  '\<\/vrf\-est\-peers\>$')
                m = p27.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['num_established_peers'] = \
                        int(m.groupdict()['num_established_peers'])
                    continue

                # <vrf-rd>1:100</vrf-rd>
                p28 = re.compile(r'^\s*\<vrf\-rd\>'
                                  '(?P<vrf_rd>([a-zA-Z0-9\:\s])+)\<\/vrf\-rd\>$')
                m = p28.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['vrf_rd'] = \
                        str(m.groupdict()['vrf_rd'])
                    continue

                # <TABLE_af>
                #  <ROW_af>
                p29 = re.compile(r'^\s*\<ROW\_af\>$')
                m = p29.match(line)
                if m:
                    if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                        parsed_dict['vrf'][vrf_name]['address_family'] = {}
                    export_rt_list = ''
                    import_rt_list = ''
                    continue

                # <af-id>0</af-id> - N/A

                # <af-name>IPv4 Unicast</af-name>
                p30 = re.compile(r'^\s*\<af\-name\>(?P<af_name>([a-zA-Z0-9\-\s])+)'
                                  '\<\/af\-name\>$')
                m = p30.match(line)
                if m:
                    address_family = str(m.groupdict()['af_name']).lower()
                    if address_family not in parsed_dict['vrf'][vrf_name]\
                        ['address_family']:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family] = {}
                        continue

                # <af-table-id>4</af-table-id>
                p31 = re.compile(r'^\s*\<af\-table\-id\>'
                                  '(?P<table_id>([a-zA-Z0-9])+)'
                                  '\<\/af\-table\-id\>$')
                m = p31.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['table_id'] = str(m.groupdict()['table_id'])
                    continue

                # <af-state>UP</af-state>
                p32 = re.compile(r'^\s*\<af-state>(?P<table_state>([a-zA-Z0-9])+)'
                                  '\<\/af\-state\>$')
                m = p32.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['table_state'] = str(m.groupdict()['table_state'])
                    continue

                # <af-num-peers>0</af-num-peers>
                p32_1 = re.compile(r'^\s*<af\-num\-peers\>'
                                  '(?P<peers>([a-zA-Z0-9])+)\<\/af\-num\-peers\>$')
                m = p32_1.match(line)
                if m:
                    if 'peers' not in parsed_dict['vrf'][vrf_name]\
                        ['address_family'][address_family]:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['peers'] = {}
                    peers = int(m.groupdict()['peers'])
                    if peers not in parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers']:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['peers'][peers] = {}
                    continue

                # <af-num-active-peers>0</af-num-active-peers>
                p33 = re.compile(r'^\s*\<af\-num\-active\-peers\>'
                                  '(?P<active_peers>([0-9])+)'
                                  '\<\/af\-num\-active\-peers\>$')
                m = p33.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['peers'][peers]['active_peers'] = \
                                int(m.groupdict()['active_peers'])
                    continue

                # <af-peer-routes>3</af-peer-routes>
                p34 = re.compile(r'^\s*\<af\-peer\-routes\>'
                                  '(?P<routes>([0-9])+)\<\/af\-peer\-routes\>$')
                m = p34.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['peers'][peers]['routes'] = \
                                int(m.groupdict()['routes'])
                    continue

                # <af-peer-paths>5</af-peer-paths>
                p35 = re.compile(r'^\s*\<af\-peer\-paths\>'
                                  '(?P<paths>([0-9])+)\<\/af\-peer\-paths\>$')
                m = p35.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['peers'][peers]['paths'] = \
                                int(m.groupdict()['paths'])
                    continue

                # <af-peer-networks>0</af-peer-networks>
                p36 = re.compile(r'^\s*\<af\-peer\-networks\>'
                                  '(?P<networks>([0-9])+)\<\/af\-peer\-networks\>$')
                m = p36.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['peers'][peers]['networks'] = int(m.groupdict()['networks'])
                    continue

                # <af-peer-aggregates>0</af-peer-aggregates>
                p37 = re.compile(r'^\s*\<af\-peer\-aggregates\>'
                                  '(?P<aggregates>([0-9])+)'
                                  '\<\/af\-peer\-aggregates\>$')
                m = p37.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['peers'][peers]['aggregates'] = \
                            int(m.groupdict()['aggregates'])
                    continue

                # <TABLE_redist>
                #   <ROW_redist>
                p38 = re.compile(r'^\s*\<ROW\_redist\>$')
                m = p38.match(line)
                if m:
                    if 'redistribution' not in parsed_dict['vrf'][vrf_name]\
                        ['address_family'][address_family]:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['redistribution'] = {}
                        continue

                #     <protocol>static</protocol>
                p39 = re.compile(r'^\s*\<protocol\>'
                                  '(?P<protocol>([a-zA-Z0-9])+)\<\/protocol\>$')
                m = p39.match(line)
                if m:
                    protocol = str(m.groupdict()['protocol'])
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['redistribution'][protocol] = {}
                    continue

                #     <route-map>ADD_RT_400_400</route-map>
                p40 = re.compile(r'^\s*\<route\-map\>'
                                  '(?P<route_map>([a-zA-Z0-9\_])+)\<\/route\-map\>$')
                m = p40.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['redistribution'][protocol]['route_map'] = \
                            str(m.groupdict()['route_map'])
                    continue

                # <af-label-mode>per-prefix</af-label-mode>
                p41 = re.compile(r'^\s*\<af\-label\-mode\>'
                                  '(?P<label_mode>([a-zA-Z0-9\_\-])+)'
                                  '\<\/af\-label\-mode\>$')
                m = p41.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['label_mode'] = str(m.groupdict()['label_mode'])
                    continue

                # <af-rr>true</af-rr>
                p42 = re.compile(r'^\s*\<af\-rr\>(?P<route_reflector>([a-zA-Z])+)'
                                  '\<\/af\-rr\>$')
                m = p42.match(line)
                if m:
                    route_reflector = str(m.groupdict()['route_reflector'])
                    if route_reflector == 'true':
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['route_reflector'] = True
                    elif route_reflector == 'false':
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['route_reflector'] = False
                    continue

                # <default-information-enabled>false</default-information-enabled> - N/A

                # <nexthop-trigger-delay-critical>3000</nexthop-trigger-delay-critical>
                p43 = re.compile(r'^\s*\<nexthop\-trigger\-delay\-critical\>'
                                  '(?P<nh_critical>([0-9])+)'
                                  '\<\/nexthop\-trigger\-delay\-critical\>$')
                m = p43.match(line)
                if m:
                    if 'next_hop_trigger_delay' not in parsed_dict['vrf']\
                        [vrf_name]['address_family'][address_family]:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['next_hop_trigger_delay'] = {}
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['next_hop_trigger_delay']['critical'] = \
                            int(m.groupdict()['nh_critical'])
                    continue

                # <nexthop-trigger-delay-non-critical>10000</nexthop-trigger-delay-non-critical>
                p44 = re.compile(r'^\s*\<nexthop\-trigger\-delay\-non\-critical\>'
                                  '(?P<nh_non_critical>([0-9])+)'
                                  '\<\/nexthop\-trigger\-delay\-non\-critical\>$')
                m = p44.match(line)
                if m:
                    if 'next_hop_trigger_delay' not in parsed_dict['vrf'][vrf_name]\
                        ['address_family'][address_family]:
                        parsed_dict['vrf'][vrf_name]['address_family']\
                            [address_family]['next_hop_trigger_delay'] = {}
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['next_hop_trigger_delay']['non_critical'] = \
                            int(m.groupdict()['nh_non_critical'])
                    continue
                
                # <af-aggregate-label>492287</af-aggregate-label>
                p45 = re.compile(r'^\s*\<af\-aggregate\-label\>'
                                  '(?P<aggregate_label>([0-9])+)'
                                  '\<\/af\-aggregate\-label\>$')
                m = p45.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['aggregate_label'] = str(m.groupdict()['aggregate_label'])
                    continue

                # <af-import-rmap>PERMIT_ALL_RM</af-import-rmap>
                # <af-export-rmap>PERMIT_ALL_RM</af-export-rmap>

                # <TABLE_evpn_export_rt>
                #  <ROW_evpn_export_rt>
                #   <evpn-export-rt>100:1</evpn-export-rt>
                p48 = re.compile(r'^\s*\<evpn\-export\-rt\>'
                                  '(?P<export_rt>([a-zA-Z0-9\:\-])+)'
                                  '\<\/evpn\-export\-rt\>$')
                m = p48.match(line)
                if m:
                    export_rt_list = \
                        export_rt_list + ' ' + m.groupdict()['export_rt']
                    export_rt_list = export_rt_list.strip()
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['export_rt_list'] = str(export_rt_list)
                    continue

                # <TABLE_evpn_import_rt>
                #  <ROW_evpn_import_rt>
                #   <evpn-import-rt>100:1</evpn-import-rt>
                p49 = re.compile(r'^\s*\<evpn\-import\-rt\>'
                                  '(?P<import_rt>([a-zA-Z0-9\:\-])+)'
                                  '\<\/evpn\-import\-rt\>$')
                m = p49.match(line)
                if m:
                    import_rt_list = \
                        import_rt_list + ' ' + m.groupdict()['import_rt']
                    import_rt_list = import_rt_list.strip()
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['import_rt_list'] = str(import_rt_list)
                    continue

                # <importdefault_prefixlimit>1000</importdefault_prefixlimit>
                p50 = re.compile(r'^\s*\<importdefault\_prefixlimit\>'
                                  '(?P<import_default_prefix_limit>([0-9])+)'
                                  '\<\/importdefault\_prefixlimit\>$')
                m = p50.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['import_default_prefix_limit'] = \
                            int(m.groupdict()['import_default_prefix_limit'])
                    continue

                # <importdefault_prefixcount>3</importdefault_prefixcount>
                p51 = re.compile(r'^\s*\<importdefault_prefixcount\>'
                                  '(?P<import_default_prefix_count>([0-9])+)'
                                  '\<\/importdefault_prefixcount\>$')
                m = p51.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['import_default_prefix_count'] = \
                            int(m.groupdict()['import_default_prefix_count'])
                    continue

                # <importdefault_map>PERMIT_ALL_RM</importdefault_map>
                p52 = re.compile(r'^\s*\<importdefault_map\>'
                                  '(?P<import_default_map>([a-zA-Z\_\-])+)'
                                  '\<\/importdefault_map\>$')
                m = p52.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['import_default_map'] = str(m.groupdict()['import_default_map'])
                    continue

                # <exportdefault_prefixlimit>1000</exportdefault_prefixlimit>
                p53 = re.compile(r'^\s*\<exportdefault_prefixlimit\>'
                                  '(?P<export_default_prefix_limit>([0-9])+)'
                                  '\<\/exportdefault_prefixlimit\>$')
                m = p53.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['export_default_prefix_limit'] = \
                            int(m.groupdict()['export_default_prefix_limit'])
                    continue

                # <exportdefault_prefixcount>2</exportdefault_prefixcount>
                p54 = re.compile(r'^\s*\<exportdefault_prefixcount\>'
                                  '(?P<export_default_prefix_count>([0-9])+)'
                                  '\<\/exportdefault_prefixcount\>$')
                m = p54.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['export_default_prefix_count'] = \
                            int(m.groupdict()['export_default_prefix_count'])
                    continue

                # <exportdefault_map>PERMIT_ALL_RM</exportdefault_map>
                p55 = re.compile(r'^\s*\<exportdefault_map\>'
                                  '(?P<export_default_map>([a-zA-Z\_\-])+)'
                                  '\<\/exportdefault_map\>$')
                m = p55.match(line)
                if m:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                        ['export_default_map'] = str(m.groupdict()['export_default_map'])
                    continue
            return parsed_dict
