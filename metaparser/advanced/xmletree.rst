.. _xmletree:

XML Parser Using ETree
""""""""""""""""""""""

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

        def xml(self):
            out = self.device.execute('show bgp process vrf all | xml')

            etree_dict = {}
            out = out.replace("]]>]]>", "")
            output = ET.fromstring(out)

            for item in output:
                for data in item:
                    for show in data:
                        for bgp in show:
                            for __XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf in bgp:
                                for process in __XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf:
                                    for __XML__OPT_Cmd_show_bgp_process_cmd_vrf in process:
                                        for __XML__OPT_Cmd_show_bgp_process_cmd___readonly__ in __XML__OPT_Cmd_show_bgp_process_cmd_vrf:
                                            for key in __XML__OPT_Cmd_show_bgp_process_cmd___readonly__:
                                                text = key.tag[key.tag.find('}')+1:]
                                                # bgp_pid
                                                if text == 'processid':
                                                    etree_dict['bgp_pid'] = int(key.text)
                                                # bgp_protocol_started_reason
                                                if text == 'protocolstartedreason':
                                                    etree_dict['bgp_protocol_started_reason'] = key.text
                                                # bgp_tag
                                                if text == 'protocoltag':
                                                    etree_dict['bgp_tag'] = key.text
                                                # bgp_protocol_state
                                                if text == 'protocolstate':
                                                    etree_dict['bgp_protocol_state'] = key.text
                                                # bgp_isolate_mode
                                                if text == 'isolatemode':
                                                    etree_dict['bgp_isolate_mode'] = key.text
                                                # bgp_mmode
                                                if text == 'mmode':
                                                    etree_dict['bgp_mmode'] = key.text
                                                # bgp_memory_state
                                                if text == 'memorystate':
                                                    etree_dict['bgp_memory_state'] = key.text
                                                # bgp_performance_mode
                                                if text == 'forwardingstatesaved':
                                                    state = key.text
                                                    if state == 'false':
                                                        etree_dict['bgp_performance_mode'] = 'No'
                                                    else:
                                                        etree_dict['bgp_performance_mode'] = 'Yes'
                                                # bgp_asformat
                                                if text == 'asformat':
                                                    etree_dict['bgp_asformat'] = key.text
                                                if text == 'srgbmin':
                                                    srgbin = key.text
                                                if text == 'srgbmax':
                                                    srgmax = key.text
                                                    try:
                                                        etree_dict['segment_routing_global_block'] = srgbin + '-' + srgmax
                                                    except:
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
                                                # bgp_paths_per_hwm_attr
                                                if text == 'pathsperattribute':
                                                    etree_dict['bgp_paths_per_hwm_attr'] = int(key.text)
                                                # bgp_as_path_entries
                                                if text == 'aspathentries':
                                                    etree_dict['bgp_as_path_entries'] = int(key.text)
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
                                                                vrf_dict['vrf_state'] = row_vrf.text
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
                                                                            af_dict['table_id'] = row_af.text
                                                                        # table_state
                                                                        if af_tag == 'af-state':
                                                                            af_dict['table_state'] = row_af.text
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
                                                                            if row_af.text == 'false':
                                                                                af_dict['route_reflector'] = False
                                                                            elif row_af.text == 'true':
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