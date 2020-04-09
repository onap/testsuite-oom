{{- define "robot.ingress.svchost._isen" -}}
	{{- $key := .key -}}
	{{- $master := .parent.Values.config.useIngressHost -}}
	{{- if hasKey $master $key -}}
		{{- $en_parent := (index $master $key) -}} 
		{{- if hasKey $en_parent "enabled" -}}
			{{- default "" (index $en_parent "enabled") -}}
		{{- else -}}
			{{- "" -}}
		{{- end -}}
	{{- else -}}
		{{- "" -}}
	{{- end -}}
{{- end -}}

{{- define "robot.ingress.svchost._port" -}}
	{{- $key := .key -}}
	{{- $master := .parent.Values.config.useIngressHost -}}
	{{- if hasKey $master $key -}}
		{{- $https_parent := (index $master $key) -}} 
		{{- if hasKey $https_parent "https" -}}
			{{- $ishttps := (index $https_parent "https") -}}
			{{- ternary 443 80 $ishttps -}}
		{{- else -}}
			{{- 80 -}}
		{{- end -}}
	{{- else -}}
		{{- 80 -}}
	{{- end -}}
{{- end -}}

{{- define "robot.ingress.svchost" -}}
 	{{- $hostname := required "service hostname" .hostname -}}
 	{{- $tplhname := $hostname | replace "-" "_" -}}
	{{- $ingress_enabled := include "robot.ingress.svchost._isen" (dict "parent" .root "key" $tplhname) -}}
	{{- if $ingress_enabled -}}
		{{- if .root.Values.global.ingress -}}
		{{- if .root.Values.global.ingress.virtualhost -}}
			{{- $domain := .root.Values.global.ingress.virtualhost.baseurl -}}
			{{- printf "%s.%s" $hostname $domain -}}
		{{- end -}}
		{{- end -}}
	{{- else -}}
		{{- $domain := include "common.namespace" .root -}}
		{{- printf "%s.%s" $hostname $domain -}}
	{{- end -}}
{{- end -}}


{{- define "robot.ingress.port" -}}
 	{{- $hostname := required "service hostname" .hostname -}}
 	{{- $port := required "service port" .port -}}
 	{{- $tplhname := $hostname | replace "-" "_" -}}
	{{- $ingress_enabled := include "robot.ingress.svchost._isen" (dict "parent" .root "key" $tplhname) -}}
	{{- if $ingress_enabled -}}
		{{- include "robot.ingress.svchost._port" (dict "parent" .root "key" $tplhname) -}}
	{{- else -}}
		{{- printf "%d" $port -}}
	{{- end -}}
{{- end -}}

