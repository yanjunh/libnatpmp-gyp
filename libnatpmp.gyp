{
  'targets': [
    {
      'target_name': 'libnatpmp',
      'type': 'static_library',
      'include_dirs': [
        '<(DEPTH)/third_party/libnatpmp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/third_party/libnatpmp',
        ],
      },
      'sources': [
        'natpmp.c',
        'getgateway.c',
      ],
      'conditions': [
        ['OS == "win"', {
          'defines': [
            'STATICLIB',
          ],
          'direct_dependent_settings': {
            'defines': [
              'STATICLIB',
            ],
            'msvs_settings': {
              'VCLinkerTool': {
                'AdditionalDependencies': [
                  'IpHlpApi.Lib',
                ],
              },
            },
          },
          'sources': [
            'wingettimeofday.c',
          ],
        }, {
          'defines': [
            'ENABLE_STRNATPMPERR',
          ],
        }],
        ['OS == "mac"', {
          'defines': [
            'MACOSX',
            '_DARWIN_C_SOURCE',
          ],
        }],
      ],
    },
    {
      'target_name': 'natpmpc-static',
      'type': 'executable',
      'sources': [
        'natpmpc.c',
      ],
      'dependencies': [
        'libnatpmp',
      ],
    },
  ],
}
