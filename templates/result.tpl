{% extends "base.tpl" %}
{% block body %}
	<div class="whois-results">
		<h2>WHOIS results</h2>
		<table>
			<tr>
				<th>WHOIS record retrieval date:</th>
				<td>{{ retrieval_date }}</td>
			</tr>
			{% if registrar != None %}
				<tr>
					<th>Registrar:</th>
					<td>{{ registrar }}</td>
				</tr>
			{% endif %}
			{% if whois_server != None %}
				<tr>
					<th>WHOIS server:</th>
					<td>{{ whois_server }}</td>
				</tr>
			{% endif %}
			{% if creation_date != None %}
				<tr>
					<th>Creation date:</th>
					<td>{{ creation_date }}</td>
				</tr>
			{% endif %}
			{% if expiration_date != None %}
				<tr>
					<th>Expiration date:</th>
					<td>{{ expiration_date }}</td>
				</tr>
			{% endif %}
			{% if updated_date != None %}
				<tr>
					<th>Record/database last updated:</th>
					<td>{{ updated_date }}</td>
				</tr>
			{% endif %}
			{% if nameservers != None %}
				{% for nameserver in nameservers %}
					<tr>
						<th>Nameserver:</th>
						<td>{{ nameserver }}</td>
					</tr>
				{% endfor %}
			{% endif %}
			{% if emails != None %}
				{% for email in emails %}
					<tr>
						<th>Contact e-mail:</th>
						<td>{{ email }}</td>
					</tr>
				{% endfor %}
			{% endif %}
			
		</table>
		<p>
			<strong>Need JSON?<strong> Try <a href="/query/json/{{ domain }}">http://whois.cryto.net/query/json/{{ domain }}</a>
		</p>
		{% if raw != None %}
			<h2>Raw WHOIS response</h2>
<pre>
{% autoescape true %}
{{ raw }}
{% endautoescape %}
</pre>
		{% endif %}
	</div>
{% endblock %}
