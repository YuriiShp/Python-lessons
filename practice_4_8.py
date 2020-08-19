m_gr = float(input('Input mass, g: '))

m_kg = round(m_gr/10**3, 3)
m_t = round(m_gr/10**6, 3)

print('Mass, kg: {}'.format(m_kg))
print('Mass, ton: {}'.format(m_t))
