#!/usr/bin/haserl
<%in p/common.cgi %>
<%
plugin="vtun"
plugin_name="Virtual Tunnel"
page_title="Virtual tunnel"
service_file=/etc/init.d/S98vtun

if [ -n "$POST_action" ] && [ "$POST_action" = "reset" ]; then
  killall tunnel
  killall vtund
  rm $service_file
  redirect_to "$SCRIPT_NAME"
fi

if [ -n "$POST_vtun_host" ]; then
  echo -e "#!/bin/sh\n\ntunnel $POST_vtun_host" > $service_file
  chmod +x $service_file
  $service_file
  redirect_to "$SCRIPT_NAME"
fi
%>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <h3>Settings</h3>
    <form action="<%= $SCRIPT_NAME %>" method="post">
<%
if [ -f "$service_file" ]; then
  ex "cat $service_file"
  field_hidden "action" "reset"
  button_submit "Reset configuration"
else
  field_text "vtun_host" "Virtual Tunnel host" "Your Virtual Tunnel server address."
  button_submit
fi
%>
    </form>
  </div>
</div>

<%in p/footer.cgi %>
